import { answerCurrent, createQuiz, getResult } from "../src/quizState.mjs";
import {
  clearPracticeWrong,
  getLessonProgress,
  getProgressSummary,
  markCurrentLesson,
  markLessonComplete,
  markPracticeWrong,
  mergeProgress,
  normalizeProgress,
  resetAllProgress,
  resolveInitialLessonIndex,
  savePracticeRun,
} from "../src/progressStore.mjs";

const lessons = Array.isArray(window.CET6_LESSONS) ? window.CET6_LESSONS : [];
const lessonById = new Map(lessons.map((lesson) => [lesson.id, lesson]));
const app = document.querySelector("#app");

// Tag every question with a globally-stable key ("<lessonId>::<number>") so
// the practice run's wrong-question list can be persisted as plain strings.
for (const lesson of lessons) {
  for (const question of lesson.questions) {
    question.__key = `${lesson.id}::${question.number}`;
  }
}
const PROGRESS_KEY = "cet6-memory-progress-v1";
const LEGACY_INDEX_KEY = "cet6-memory-lesson-index";
const SYNC_URL = "/api/progress";
const PUSH_DEBOUNCE_MS = 600;
const SYNC_LABELS = {
  local: "本地",
  syncing: "同步中…",
  synced: "已同步",
  offline: "离线（仅本机保存）",
};
const DIGIT_LABELS = new Map([
  ["1", "A"],
  ["2", "B"],
  ["3", "C"],
  ["4", "D"],
]);
const FEEDBACK_MS = { correct: 650, wrong: 1600 };
const CELEBRATE_THRESHOLD = 0.8;
const ICON_CHECK = `<svg class="review-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M4 12.5L9.5 18L20 6" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const ICON_CROSS = `<svg class="review-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M6 6L18 18M18 6L6 18" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>`;

let progress = loadProgress();
let state = {
  lessonIndex: 0,
  mode: "study",
  quiz: null,
  review: null,
  navDir: null,
  practiceBatchStart: 0,
  batchStartedAt: 0,
};
let pendingTimer = 0;
let pushTimer = 0;
let syncState = "local";
let refreshing = false;
let practiceStartedAt = 0;
let practiceElapsedFrozen = 0;
let practiceTimerHandle = 0;

boot();

async function boot() {
  if (lessons.length === 0) {
    render();
    return;
  }

  app.innerHTML = `<main class="shell"><div class="empty">正在载入进度…</div></main>`;
  const server = await fetchServerProgress(2000);
  if (server) {
    progress = mergeProgress(progress, server);
    syncState = "synced";
  } else {
    syncState = "offline";
  }

  const legacyIndex = Number(localStorage.getItem(LEGACY_INDEX_KEY) || 0);
  const initialIndex = progress.currentLessonId
    ? resolveInitialLessonIndex(progress, lessons)
    : clamp(legacyIndex, 0, Math.max(lessons.length - 1, 0));
  state = { ...state, lessonIndex: initialIndex };
  progress = markCurrentLesson(progress, lessons[initialIndex]);
  saveProgress();

  document.addEventListener("keydown", onKeydown);
  document.addEventListener("pointerdown", onRipplePointerDown);
  window.addEventListener("focus", pullServerProgress);
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden") flushPendingPush();
    else pullServerProgress();
  });

  if (location.hash === "#practice") {
    startPractice();
  } else {
    render();
  }
}

function prefersReducedMotion() {
  return window.matchMedia?.("(prefers-reduced-motion: reduce)").matches ?? false;
}

// Delegated on `document` (not #app) so it survives every innerHTML re-render.
function onRipplePointerDown(event) {
  if (prefersReducedMotion()) return;
  const button = event.target.closest("button");
  if (!button || button.disabled) return;
  const rect = button.getBoundingClientRect();
  const size = Math.max(rect.width, rect.height) * 1.6;
  const ripple = document.createElement("span");
  ripple.className = "ripple";
  ripple.style.width = `${size}px`;
  ripple.style.height = `${size}px`;
  ripple.style.left = `${event.clientX - rect.left - size / 2}px`;
  ripple.style.top = `${event.clientY - rect.top - size / 2}px`;
  ripple.addEventListener("animationend", () => ripple.remove());
  button.appendChild(ripple);
}

function onKeydown(event) {
  if (event.altKey || event.ctrlKey || event.metaKey) return;
  if (lessons.length === 0) return;
  const target = event.target;
  if (
    target instanceof HTMLElement &&
    target.closest("select, input, textarea, button, summary, a")
  ) {
    return;
  }

  if (state.mode === "study") {
    if (event.key === "Enter") {
      event.preventDefault();
      startQuiz();
    }
    if (event.key === "ArrowRight") moveLesson(1);
    if (event.key === "ArrowLeft") moveLesson(-1);
    return;
  }

  if (event.key === "Escape") {
    backToStudy();
    return;
  }
  if (state.mode === "wrongbook") return;
  if (state.review) return;
  if (state.quiz?.isComplete) {
    if (event.key === "Enter") {
      event.preventDefault();
      if (state.mode === "practice") {
        if (isFinalPracticeBatch()) backToStudy();
        else continueToNextBatch();
      } else {
        moveLesson(1);
      }
    }
    if (event.key.toUpperCase() === "R") retryCurrent();
    return;
  }

  const label = keyToLabel(event.key);
  if (!label) return;
  const question = currentQuestion();
  if (!question.options.some((option) => option.label === label)) return;
  submitAnswer(label);
}

function keyToLabel(key) {
  const upper = key.toUpperCase();
  if (["A", "B", "C", "D"].includes(upper)) return upper;
  return DIGIT_LABELS.get(key) || "";
}

function render() {
  if (lessons.length === 0) {
    app.innerHTML = `
      <main class="shell">
        <div class="empty">没有可加载的题库数据，请先运行 npm run build:data。</div>
      </main>
    `;
    return;
  }

  const navDir = state.navDir;
  if (navDir) state = { ...state, navDir: null };

  app.innerHTML = `
    <main class="shell">
      ${
        state.mode === "study"
          ? `${renderTopbar()}${renderProgress()}${renderStudy(navDir)}`
          : state.mode === "wrongbook"
            ? renderWrongbook()
            : renderQuiz()
      }
    </main>
  `;

  bindEvents();

  if (state.quiz?.isComplete && !state.review) {
    animateScoreCount();
  }
}

// Runs the score straight to its final value in the same synchronous tick,
// then rAF-animates the count-up — avoids a one-frame flash of "0/N".
function animateScoreCount() {
  const el = app.querySelector(".score[data-correct]");
  if (!el) return;
  const correct = Number(el.dataset.correct);
  const total = Number(el.dataset.total);
  if (prefersReducedMotion() || correct === 0) {
    el.textContent = `${correct}/${total}`;
    return;
  }
  const duration = 550;
  const start = performance.now();
  const step = (now) => {
    const elapsed = Math.min(1, (now - start) / duration);
    const eased = 1 - (1 - elapsed) ** 3;
    el.textContent = `${Math.round(eased * correct)}/${total}`;
    if (elapsed < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

function practiceButtonLabel() {
  const { order, index } = progress.practice;
  if (order.length > 0 && index > 0 && index < order.length) {
    return `继续练习（已做 ${index}/${order.length} 篇）`;
  }
  return `直接练习全部题目（${lessons.length}篇 · 按年份从2016年开始）`;
}

function renderTopbar() {
  const lesson = currentLesson();
  const summary = getProgressSummary(progress, lessons);
  return `
    <section class="topbar">
      <div style="min-width: 0">
        <p class="eyebrow">CET6 Section C Memory</p>
        <h1>${escapeHtml(lesson.title)}</h1>
        <p class="subtle">已背 ${summary.completed}/${summary.total} 篇 · 进度自动保存 · Enter 开始测验，←/→ 切换文章</p>
      </div>
      <div class="toolbar">
        <select class="select" data-action="select-lesson" aria-label="选择文章">
          ${lessons
            .map(
              (item, index) => {
                const done = getLessonProgress(progress, item)?.completed;
                return `
                <option value="${index}" ${index === state.lessonIndex ? "selected" : ""}>
                  ${done ? "✓" : "○"} ${index + 1}. ${escapeHtml(item.title)}
                </option>
              `;
              },
            )
            .join("")}
        </select>
        <button class="ghost-button" data-action="previous">上一篇</button>
        <button class="ghost-button" data-action="next">下一篇</button>
        <button class="ghost-button" data-action="next-incomplete">下一个未背</button>
        <span class="toolbar-divider" aria-hidden="true"></span>
        <button class="primary-button" data-action="start-practice">${practiceButtonLabel()}</button>
        <button class="ghost-button" data-action="open-wrongbook">错题本（${wrongCount()}）</button>
        <span class="toolbar-divider" aria-hidden="true"></span>
        <button class="ghost-button danger compact" data-action="reset-practice">重置刷题进度</button>
        <button class="ghost-button danger compact" data-action="reset-progress">重置进度</button>
      </div>
    </section>
  `;
}

function renderProgress() {
  const summary = getProgressSummary(progress, lessons);
  return `
    <div class="progress-wrap">
      <div class="progress-track" aria-hidden="true">
        <div class="progress-fill" style="--progress: ${summary.percent}%"></div>
      </div>
      <div class="progress-label">已完成 ${summary.percent}% · 当前第 ${state.lessonIndex + 1} / ${lessons.length} 篇 · <span id="sync-status" data-state="${syncState}">${SYNC_LABELS[syncState]}</span></div>
    </div>
  `;
}

function renderStudy(navDir) {
  const lesson = currentLesson();
  const saved = getLessonProgress(progress, lesson);
  const navClass = navDir === "next" ? "slide-next" : navDir === "prev" ? "slide-prev" : "";
  return `
    <section class="study-grid ${navClass}">
      <article class="panel">
        <div class="panel-inner">
          <div class="meta-row">
            <span class="pill">${escapeHtml(lesson.examDate)}</span>
            <span class="pill">${escapeHtml(lesson.passageLabel)}</span>
            <span class="pill">5 Questions</span>
            ${
              saved
                ? `<span class="pill">最好 ${saved.bestCorrect}/${saved.total}</span><span class="pill">${saved.attempts} 次</span>${saved.bestTimeMs != null ? `<span class="pill">最快 ${formatElapsed(saved.bestTimeMs)}</span>` : ""}`
                : `<span class="pill">未完成</span>`
            }
          </div>
          <div class="gist">
            <div class="gist-block">
              <div class="gist-label">中文大意</div>
              <p class="gist-text">${escapeHtml(lesson.mainIdeaZh)}</p>
            </div>
            <div class="gist-block en">
              <div class="gist-label">English Gist</div>
              <p class="gist-text">${escapeHtml(lesson.mainIdeaEn)}</p>
            </div>
            <div class="mnemonic-block">
              <div class="gist-label">五题答案口诀</div>
              <p class="mnemonic-text">${escapeHtml(lesson.answerMnemonic || "")}</p>
              <div class="answer-code">答案串（辅助）：${escapeHtml(lesson.answerCode || "")}</div>
            </div>
          </div>
        </div>
      </article>

      <section class="question-list">
        ${lesson.questions.map(renderMemoryCard).join("")}
        <button class="primary-button" data-action="start-quiz">我已经背完，开始纯英文测验（Enter）</button>
      </section>
    </section>
  `;
}

// Read-only review of every question currently marked wrong in practice mode
// (progress.practice.wrong). A question drops out automatically the next
// time it's answered correctly, so this list only ever shows what's left to
// master, not a growing permanent log.
function renderWrongbook() {
  const keys = Object.keys(progress.practice.wrong || {});
  const items = keys.map(lookupQuestion).filter(Boolean);
  return `
    <section class="topbar">
      <div>
        <p class="eyebrow">错题本</p>
        <h1>还没做对的题（${items.length}）</h1>
        <p class="subtle">在"直接练习全部题目"里重新做对一次，会自动从这里移除 · Esc 返回</p>
      </div>
      <div class="toolbar">
        <button class="ghost-button" data-action="back-study">返回</button>
      </div>
    </section>
    <section class="question-list">
      ${
        items.length > 0
          ? items.map(renderMemoryCard).join("")
          : `<div class="empty">还没有错题，继续保持！</div>`
      }
    </section>
  `;
}

function lookupQuestion(key) {
  const [lessonId, number] = key.split("::");
  const lesson = lessonById.get(lessonId);
  return lesson?.questions.find((question) => question.number === number) || null;
}

function openWrongbook() {
  window.clearTimeout(pendingTimer);
  state = { ...state, mode: "wrongbook", quiz: null, review: null };
  render();
}

function renderMemoryCard(question) {
  return `
    <article class="memory-card">
      <div class="memory-head">
        <span class="question-number">${escapeHtml(question.number)}</span>
        <span class="answer-chip">${escapeHtml(question.answer || "-")}</span>
      </div>
      <div class="question-label">中文题目</div>
      <p class="zh-prompt">${escapeHtml(question.questionZh)}</p>
      <div class="question-label">English Question</div>
      <p class="en-stem">${escapeHtml(question.stem)}</p>
      <p class="answer-line">
        <strong>答案：</strong>${escapeHtml(question.answer || "-")}. ${escapeHtml(question.answerText || "暂无答案文本")}
      </p>
      <p class="answer-zh">
        <strong>答案中文：</strong>${escapeHtml(question.answerZh || "暂无答案中文意思")}
      </p>
      ${
        question.explanation
          ? `
      <details class="explain">
        <summary>答案解析</summary>
        <p>${escapeHtml(question.explanation)}</p>
      </details>`
          : ""
      }
    </article>
  `;
}

function renderQuiz() {
  if (state.quiz?.isComplete && !state.review) return renderResult();

  const lesson = state.quiz.lesson;
  const review = state.review;
  const question = review ? review.question : currentQuestion();
  const position = review ? state.quiz.answers.length : state.quiz.currentIndex + 1;
  return `
    ${state.mode === "practice" ? renderPracticeProgress() : ""}
    <section class="panel quiz-panel">
      <div class="panel-inner">
        <div class="meta-row">
          <span class="pill">Question ${position} / ${lesson.questions.length}</span>
          <span class="pill">${escapeHtml(lesson.examDate)}</span>
          <span class="pill">${escapeHtml(lesson.passageLabel)}</span>
          <button class="ghost-button compact push-right" data-action="back-study">Esc 返回背诵</button>
        </div>
        <h2 class="quiz-question">${escapeHtml(question.stem)}</h2>
        <div class="option-grid ${review ? "reviewed" : ""}">
          ${question.options.map((option) => renderOption(option, review)).join("")}
        </div>
        <div class="feedback-area" aria-live="polite">
          ${
            review
              ? renderFeedback(review.answer)
              : `<div class="feedback hint">点击选项或按 A–D / 1–4 作答</div>`
          }
        </div>
      </div>
    </section>
  `;
}

// Own progress bar for the "practice all questions" page — separate from
// renderProgress()'s per-lesson study-completion bar. Tracks the persisted
// position across the whole year-grouped run (survives leaving and coming
// back), one passage = one step.
function renderPracticeProgress() {
  const totalLessons = progress.practice.order.length || lessons.length;
  const doneLessons = state.practiceBatchStart;
  const totalQuestions = totalLessons * 5;
  const doneQuestions = doneLessons * 5 + state.quiz.answers.length;
  const percent = totalQuestions === 0 ? 0 : Math.round((doneQuestions / totalQuestions) * 100);
  return `
    <div class="progress-wrap">
      <div class="progress-track" aria-hidden="true">
        <div class="progress-fill" style="--progress: ${percent}%"></div>
      </div>
      <div class="progress-label">刷题练习 · 第 ${doneLessons + 1}/${totalLessons} 篇（${state.quiz.lesson.year} 年） · 已完成 ${doneQuestions}/${totalQuestions} 题（${percent}%） · 错题本 ${wrongCount()} 道 · 用时 <span id="practice-timer">${formatElapsed(Date.now() - practiceStartedAt)}</span></div>
    </div>
  `;
}

function renderOption(option, review) {
  let className = "option-button";
  if (review) {
    if (option.label === review.answer.correct) className += " correct";
    else if (option.label === review.answer.selected) className += " wrong";
    else className += " dimmed";
  }
  return `
    <button class="${className}" data-action="answer" data-answer="${escapeHtml(option.label)}" ${review ? "disabled" : ""}>
      <span class="option-letter">${escapeHtml(option.label)}</span>
      <span class="option-text">${escapeHtml(option.text)}</span>
    </button>
  `;
}

function renderFeedback(answer) {
  const className = answer.isCorrect ? "good" : "bad";
  const icon = answer.isCorrect ? ICON_CHECK : ICON_CROSS;
  const text = answer.isCorrect
    ? `Correct — ${answer.correct}`
    : `正确答案 ${answer.correct}. ${answer.correctText}`;
  return `<div class="feedback ${className}">${icon}<span>${escapeHtml(text)}</span></div>`;
}

function renderResult() {
  const result = getResult(state.quiz);
  const lesson = state.quiz.lesson;
  const isPractice = state.mode === "practice";
  const practiceDone = isPractice && isFinalPracticeBatch();
  const saved = getLessonProgress(progress, lesson);
  const thisBatchMs = Date.now() - state.batchStartedAt;
  const isBestTime = saved?.bestTimeMs != null && saved.bestTimeMs >= thisBatchMs;
  const batchTimeLine = `这5题用时 ${formatElapsed(thisBatchMs)}${isBestTime ? "（本篇最快）" : saved?.bestTimeMs != null ? ` · 最快 ${formatElapsed(saved.bestTimeMs)}` : ""}`;
  return `
    <section class="panel quiz-panel result">
      <div class="panel-inner">
        <p class="eyebrow">Result</p>
        <h2>${practiceDone ? "全部题库练习完成" : "Passage Complete"}</h2>
        <div class="score" data-correct="${result.correct}" data-total="${result.total}">0/${result.total}</div>
        <p class="subtle">${result.percent}% correct · 答案串：${escapeHtml(lesson.answerCode || "")} · ${batchTimeLine}${isPractice ? ` · 累计用时 ${formatElapsed(practiceDone ? practiceElapsedFrozen : Date.now() - practiceStartedAt)} · 错题本 ${wrongCount()} 道` : ""}</p>
        <div class="review-list">
          ${state.quiz.answers.map(renderReviewRow).join("")}
        </div>
        <div class="result-actions">
          <button class="ghost-button" data-action="retry">Retry（R）</button>
          ${
            isPractice
              ? practiceDone
                ? `<button class="primary-button" data-action="back-study">完成，返回（Enter）</button>`
                : `<button class="primary-button" data-action="continue-practice">继续下一组（Enter）</button>`
              : `<button class="primary-button" data-action="next">Next Passage（Enter）</button>`
          }
        </div>
      </div>
    </section>
  `;
}

function wrongCount() {
  return Object.keys(progress.practice.wrong || {}).length;
}

function renderReviewRow(answer, index) {
  const question = state.quiz.lesson.questions[index];
  const detail = answer.isCorrect
    ? `${answer.correct}. ${answer.correctText}`
    : `你选 ${answer.selected} → 正确 ${answer.correct}. ${answer.correctText}`;
  return `
    <div class="review-row ${answer.isCorrect ? "good" : "bad"}">
      <span class="review-mark">${answer.isCorrect ? ICON_CHECK : ICON_CROSS}</span>
      <div>
        <p class="review-stem">${escapeHtml(question.number)}. ${escapeHtml(question.stem)}</p>
        ${
          question.questionZh
            ? `<p class="review-stem-zh">题目：${escapeHtml(question.questionZh)}</p>`
            : ""
        }
        <p class="review-answer">${escapeHtml(detail)}</p>
        ${
          question.answerZh
            ? `<p class="review-zh">中文：${escapeHtml(question.answerZh)}</p>`
            : ""
        }
      </div>
    </div>
  `;
}

function bindEvents() {
  app.querySelectorAll("[data-action]").forEach((element) => {
    element.addEventListener("click", () => {
      const action = element.dataset.action;
      if (action === "start-quiz") startQuiz();
      if (action === "answer") submitAnswer(element.dataset.answer);
      if (action === "next") moveLesson(1);
      if (action === "previous") moveLesson(-1);
      if (action === "next-incomplete") jumpToNextIncomplete();
      if (action === "retry") retryCurrent();
      if (action === "reset-progress") resetProgress();
      if (action === "back-study") backToStudy();
      if (action === "start-practice") startPractice();
      if (action === "continue-practice") continueToNextBatch();
      if (action === "open-wrongbook") openWrongbook();
      if (action === "reset-practice") resetPracticeProgress();
    });
  });

  app.querySelector("[data-action='select-lesson']")?.addEventListener("change", (event) => {
    setLesson(Number(event.target.value));
  });
}

function startQuiz() {
  window.clearTimeout(pendingTimer);
  progress = markCurrentLesson(progress, currentLesson());
  saveProgress();
  state = {
    ...state,
    mode: "quiz",
    quiz: createQuiz(currentLesson()),
    review: null,
    batchStartedAt: Date.now(),
  };
  render();
}

// "直接练习全部题目" — walks through every lesson (real passage + its own 5
// questions in their original order, never mixed with another passage's)
// directly in quiz mode, no study/memorize step first. Passages are worked
// through strictly in sequence, year-by-year starting from 2016, no
// shuffling anywhere. Each passage is its own checkpoint/score screen —
// same as a normal single-lesson quiz. The run's order + current position
// are persisted so
// leaving and coming back resumes at the next unseen passage.
function startPractice() {
  window.clearTimeout(pendingTimer);
  ensurePracticeOrder();
  startPracticeTimer();
  openPracticeBatch(progress.practice.order, progress.practice.index);
}

// (Re)builds a fresh full run only when there's no run in progress, or the
// previous run has been fully worked through.
function ensurePracticeOrder() {
  const { order, index } = progress.practice;
  if (order.length === 0 || index >= order.length) {
    const freshOrder = buildYearGroupedLessonOrder();
    progress = savePracticeRun(progress, freshOrder, 0);
    saveProgress();
  }
}

// Straight sequential order: grouped by year ascending (2016 first), and
// within a year kept exactly in the dataset's original order — no shuffling
// anywhere, so a run always walks the same fixed sequence.
function buildYearGroupedLessonOrder() {
  const byYear = new Map();
  for (const lesson of lessons) {
    const year = lesson.year || "0000";
    if (!byYear.has(year)) byYear.set(year, []);
    byYear.get(year).push(lesson.id);
  }
  return Array.from(byYear.keys())
    .sort()
    .flatMap((year) => byYear.get(year));
}

// One batch = one full passage (its real 5 questions, in original order) —
// reuses the exact same quiz UI/flow as a normal single-lesson quiz.
function openPracticeBatch(order, batchIndex) {
  const lesson = lessonById.get(order[batchIndex]) || lessons[0];
  state = {
    ...state,
    mode: "practice",
    quiz: createQuiz(lesson),
    review: null,
    practiceBatchStart: batchIndex,
    batchStartedAt: Date.now(),
  };
  if (location.hash !== "#practice") history.replaceState(null, "", "#practice");
  render();
}

function continueToNextBatch() {
  openPracticeBatch(progress.practice.order, progress.practice.index);
}

function isFinalPracticeBatch() {
  return state.practiceBatchStart + 1 >= progress.practice.order.length;
}

function startPracticeTimer() {
  window.clearInterval(practiceTimerHandle);
  practiceStartedAt = Date.now();
  practiceElapsedFrozen = 0;
  practiceTimerHandle = window.setInterval(tickPracticeTimer, 1000);
}

function stopPracticeTimer() {
  window.clearInterval(practiceTimerHandle);
  practiceTimerHandle = 0;
}

function tickPracticeTimer() {
  if (state.mode !== "practice") {
    stopPracticeTimer();
    return;
  }
  const el = document.querySelector("#practice-timer");
  if (el) el.textContent = formatElapsed(Date.now() - practiceStartedAt);
}

function formatElapsed(ms) {
  const totalSeconds = Math.max(0, Math.floor(ms / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return hours > 0
    ? `${hours}:${pad(minutes)}:${pad(seconds)}`
    : `${pad(minutes)}:${pad(seconds)}`;
}

function retryCurrent() {
  // Retry only redoes the current 5-question batch — the run's checkpoint
  // has already moved past it, so this doesn't affect resume position.
  if (state.mode === "practice") openPracticeBatch(progress.practice.order, state.practiceBatchStart);
  else startQuiz();
}

function backToStudy() {
  window.clearTimeout(pendingTimer);
  stopPracticeTimer();
  state = { ...state, mode: "study", quiz: null, review: null };
  if (location.hash === "#practice") {
    history.replaceState(null, "", location.pathname + location.search);
  }
  render();
}

function submitAnswer(label) {
  if (state.review || !state.quiz || state.quiz.isComplete) return;

  const question = currentQuestion();
  const nextQuiz = answerCurrent(state.quiz, label);
  const answer = nextQuiz.answers.at(-1);
  state = { ...state, quiz: nextQuiz, review: { question, answer } };

  if (state.mode === "practice" && question.__key) {
    progress = answer.isCorrect
      ? clearPracticeWrong(progress, question.__key)
      : markPracticeWrong(progress, question.__key);
  }

  if (nextQuiz.isComplete) {
    const batchTimeMs = Date.now() - state.batchStartedAt;
    progress = markLessonComplete(progress, nextQuiz.lesson, getResult(nextQuiz), batchTimeMs);

    if (state.mode === "practice") {
      // Checkpoint: persist how far into the run we've gotten (one passage
      // per step), so leaving now resumes at the next unseen passage.
      const nextIndex = state.practiceBatchStart + 1;
      progress = savePracticeRun(progress, progress.practice.order, nextIndex);
      if (nextIndex >= progress.practice.order.length) {
        practiceElapsedFrozen = Date.now() - practiceStartedAt;
        stopPracticeTimer();
      }
    }

    saveProgress();
  } else if (state.mode === "practice") {
    // Persist wrong/cleared marks as they happen, not just at the batch
    // checkpoint — otherwise closing mid-batch loses this answer's mark.
    saveProgress();
  }

  render();
  schedule(() => {
    state = { ...state, review: null };
    render();
    if (nextQuiz.isComplete) {
      const result = getResult(nextQuiz);
      if (result.total > 0 && result.correct / result.total >= CELEBRATE_THRESHOLD) {
        launchConfetti();
      }
    }
  }, answer.isCorrect ? FEEDBACK_MS.correct : FEEDBACK_MS.wrong);
}

// One-shot canvas particle burst; the canvas removes itself once every
// particle has faded or fallen off-screen. Skipped under reduced motion.
function launchConfetti() {
  if (prefersReducedMotion()) return;

  const canvas = document.createElement("canvas");
  canvas.className = "confetti-canvas";
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  document.body.appendChild(canvas);

  const ctx = canvas.getContext("2d");
  const colors = ["#0f766e", "#1d4ed8", "#b45309", "#9f1239", "#0ea5a3", "#f59e0b"];
  const particles = Array.from({ length: 80 }, () => ({
    x: canvas.width / 2 + (Math.random() - 0.5) * 220,
    y: canvas.height * 0.32,
    vx: (Math.random() - 0.5) * 9,
    vy: -Math.random() * 8 - 3,
    size: Math.random() * 6 + 4,
    color: colors[Math.floor(Math.random() * colors.length)],
    rotation: Math.random() * Math.PI,
    spin: (Math.random() - 0.5) * 0.3,
    rect: Math.random() < 0.5,
  }));
  const gravity = 0.26;
  const duration = 1700;
  const start = performance.now();

  function frame(now) {
    const elapsed = now - start;
    const fade = Math.max(0, 1 - elapsed / duration);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (fade <= 0) {
      canvas.remove();
      return;
    }

    for (const p of particles) {
      p.vy += gravity;
      p.x += p.vx;
      p.y += p.vy;
      p.rotation += p.spin;
      if (p.y > canvas.height + 40) continue;

      ctx.save();
      ctx.globalAlpha = fade;
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rotation);
      ctx.fillStyle = p.color;
      if (p.rect) ctx.fillRect(-p.size / 2, -p.size / 3, p.size, p.size * 0.66);
      else {
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    }

    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);
}

function schedule(callback, delay) {
  window.clearTimeout(pendingTimer);
  pendingTimer = window.setTimeout(callback, delay);
}

// Scans forward (wrapping) from the current lesson for the next one without
// a completed attempt, so a 124-lesson deck doesn't force sequential paging.
function jumpToNextIncomplete() {
  for (let step = 1; step <= lessons.length; step += 1) {
    const index = (state.lessonIndex + step) % lessons.length;
    if (!getLessonProgress(progress, lessons[index])?.completed) {
      setLesson(index, "next");
      return;
    }
  }
}

function moveLesson(offset) {
  setLesson(
    (state.lessonIndex + offset + lessons.length) % lessons.length,
    offset > 0 ? "next" : "prev",
  );
}

function setLesson(index, navDir = null) {
  window.clearTimeout(pendingTimer);
  const lessonIndex = clamp(index, 0, lessons.length - 1);
  state = {
    lessonIndex,
    mode: "study",
    quiz: null,
    review: null,
    navDir,
    practiceBatchStart: 0,
    batchStartedAt: 0,
  };
  progress = markCurrentLesson(progress, lessons[lessonIndex]);
  saveProgress();
  render();
}

function resetProgress() {
  if (!window.confirm("确定要重置所有背诵进度吗？重置会同步到所有设备。")) return;
  window.clearTimeout(pendingTimer);
  progress = resetAllProgress(currentLesson());
  saveProgress();
  render();
}

// Escape hatch for "直接练习全部题目" getting into a stuck/inconsistent
// state. This is a *hard* reset: it wipes the local cache and reloads
// instead of just overwriting the in-memory `progress` and pushing — an
// in-memory reset still gets synced against the server via mergeProgress's
// "newer updatedAt wins" rule, so a stale local copy (e.g. one that ever
// adopted a corrupted/future-dated updatedAt) can silently win the merge
// and undo the reset. Wiping localStorage removes that stale copy entirely,
// so the fresh boot has nothing left to lose the merge to and correctly
// re-adopts the server's copy (lesson completion history included, since
// mergeProgress unions lesson entries from whichever side has them).
function resetPracticeProgress() {
  if (!window.confirm('确定要重置"直接练习全部题目"的进度和错题本吗？（不会影响背诵进度，会刷新页面）')) return;
  localStorage.removeItem(PROGRESS_KEY);
  localStorage.removeItem(LEGACY_INDEX_KEY);
  location.reload();
}

function currentLesson() {
  return lessons[state.lessonIndex];
}

function currentQuestion() {
  return state.quiz.lesson.questions[state.quiz.currentIndex];
}

function clamp(value, min, max) {
  if (Number.isNaN(value)) return min;
  return Math.min(Math.max(value, min), max);
}

function loadProgress() {
  try {
    return normalizeProgress(JSON.parse(localStorage.getItem(PROGRESS_KEY) || "null"));
  } catch {
    return normalizeProgress(null);
  }
}

function saveProgress() {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
  localStorage.setItem(LEGACY_INDEX_KEY, String(state.lessonIndex));
  schedulePush();
}

async function fetchServerProgress(timeoutMs) {
  try {
    const controller = new AbortController();
    const timer = window.setTimeout(() => controller.abort(), timeoutMs);
    const response = await fetch(SYNC_URL, {
      signal: controller.signal,
      cache: "no-store",
    });
    window.clearTimeout(timer);
    if (!response.ok) return null;
    return await response.json();
  } catch {
    return null;
  }
}

function schedulePush() {
  window.clearTimeout(pushTimer);
  pushTimer = window.setTimeout(pushProgress, PUSH_DEBOUNCE_MS);
}

async function pushProgress() {
  setSyncState("syncing");
  try {
    const response = await fetch(SYNC_URL, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(progress),
    });
    if (!response.ok) throw new Error(String(response.status));
    adoptProgress(await response.json());
    setSyncState("synced");
  } catch {
    setSyncState("offline");
  }
}

// 页面切到后台/关闭时，把可能还在防抖等待中的进度立刻发出去。
function flushPendingPush() {
  window.clearTimeout(pushTimer);
  navigator.sendBeacon?.(
    SYNC_URL,
    new Blob([JSON.stringify(progress)], { type: "application/json" }),
  );
}

// 切回页面时拉取服务器进度：合并成绩；若其他设备的进度更新，跳到它的学习位置。
async function pullServerProgress() {
  if (document.visibilityState !== "visible" || refreshing) return;
  refreshing = true;
  try {
    const server = await fetchServerProgress(3000);
    if (!server) {
      setSyncState("offline");
      return;
    }
    const before = JSON.stringify(progress);
    const remoteNewer =
      (server.updatedAt || "") > (progress.updatedAt || "");
    const merged = mergeProgress(progress, server);
    if (JSON.stringify(merged) !== before) {
      progress = merged;
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
      if (remoteNewer && state.mode === "study") {
        state = {
          ...state,
          lessonIndex: resolveInitialLessonIndex(progress, lessons),
        };
      }
      if (state.mode === "study") render();
      schedulePush();
    }
    setSyncState("synced");
  } finally {
    refreshing = false;
  }
}

function adoptProgress(next) {
  const incoming = normalizeProgress(next);
  if (JSON.stringify(incoming) === JSON.stringify(progress)) return;
  progress = incoming;
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
  if (state.mode === "study") render();
}

function setSyncState(next) {
  syncState = next;
  const element = document.querySelector("#sync-status");
  if (element) {
    element.textContent = SYNC_LABELS[next];
    element.dataset.state = next;
  }
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
