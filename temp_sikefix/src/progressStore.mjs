function nowIso() {
  return new Date().toISOString();
}

export function createEmptyProgress() {
  return {
    version: 1,
    currentLessonId: "",
    updatedAt: "",
    resetAt: "",
    lessons: {},
    practice: { order: [], index: 0, wrong: {} },
  };
}

function normalizePractice(value) {
  const raw = value && typeof value === "object" ? value : {};
  return {
    order: Array.isArray(raw.order)
      ? raw.order.filter((item) => typeof item === "string")
      : [],
    index: Number.isInteger(raw.index) && raw.index >= 0 ? raw.index : 0,
    wrong: raw.wrong && typeof raw.wrong === "object" ? raw.wrong : {},
  };
}

export function normalizeProgress(value) {
  if (!value || typeof value !== "object") return createEmptyProgress();
  return {
    version: 1,
    currentLessonId:
      typeof value.currentLessonId === "string" ? value.currentLessonId : "",
    updatedAt: typeof value.updatedAt === "string" ? value.updatedAt : "",
    resetAt: typeof value.resetAt === "string" ? value.resetAt : "",
    lessons:
      value.lessons && typeof value.lessons === "object" ? value.lessons : {},
    practice: normalizePractice(value.practice),
  };
}

export function markCurrentLesson(progress, lesson) {
  return {
    ...normalizeProgress(progress),
    currentLessonId: lesson?.id || "",
    updatedAt: nowIso(),
  };
}

// timeMs (optional) is how long this attempt at the 5 questions took —
// tracked per lesson (bestTimeMs = fastest ever, lastTimeMs = most recent),
// same "one lesson at a time" granularity whether reached via normal study
// mode or via "直接练习全部题目".
export function markLessonComplete(progress, lesson, result, timeMs) {
  const normalized = normalizeProgress(progress);
  const existing = normalized.lessons[lesson.id] || {};
  const bestCorrect = Math.max(existing.bestCorrect || 0, result.correct);
  const bestPercent = Math.max(existing.bestPercent || 0, result.percent);
  const validTime = typeof timeMs === "number" && Number.isFinite(timeMs) && timeMs > 0 ? timeMs : null;
  const bestTimeMs = minPositive(existing.bestTimeMs, validTime);

  return {
    ...normalized,
    currentLessonId: normalized.currentLessonId || lesson.id,
    updatedAt: nowIso(),
    lessons: {
      ...normalized.lessons,
      [lesson.id]: {
        completed: true,
        attempts: (existing.attempts || 0) + 1,
        bestCorrect,
        bestPercent,
        bestTimeMs,
        lastTimeMs: validTime ?? existing.lastTimeMs ?? null,
        total: result.total,
        completedAt: nowIso(),
      },
    },
  };
}

function minPositive(...values) {
  const positives = values.filter((value) => typeof value === "number" && value > 0);
  return positives.length ? Math.min(...positives) : null;
}

// 「直接练习全部题目」的题序 + 断点，退出后下次能从原来的位置继续。
export function savePracticeRun(progress, order, index) {
  const normalized = normalizeProgress(progress);
  return {
    ...normalized,
    updatedAt: nowIso(),
    practice: { ...normalized.practice, order, index },
  };
}

export function markPracticeWrong(progress, questionKey) {
  const normalized = normalizeProgress(progress);
  return {
    ...normalized,
    updatedAt: nowIso(),
    practice: {
      ...normalized.practice,
      wrong: { ...normalized.practice.wrong, [questionKey]: true },
    },
  };
}

// 之后重新做对了，就把它从错题本里摘掉。
export function clearPracticeWrong(progress, questionKey) {
  const normalized = normalizeProgress(progress);
  const wrong = { ...normalized.practice.wrong };
  delete wrong[questionKey];
  return {
    ...normalized,
    updatedAt: nowIso(),
    practice: { ...normalized.practice, wrong },
  };
}

export function resetAllProgress(lesson) {
  const now = nowIso();
  return {
    ...createEmptyProgress(),
    currentLessonId: lesson?.id || "",
    updatedAt: now,
    resetAt: now,
  };
}

// 合并两份进度（本机与服务器/其他设备）。逐课取最好成绩，
// currentLessonId 跟随 updatedAt 较新的一侧；resetAt 之前完成的记录视为已重置。
export function mergeProgress(a, b) {
  const left = normalizeProgress(a);
  const right = normalizeProgress(b);
  const resetAt = later(left.resetAt, right.resetAt);
  const newer = (right.updatedAt || "") > (left.updatedAt || "") ? right : left;

  const lessons = {};
  const ids = new Set([
    ...Object.keys(left.lessons),
    ...Object.keys(right.lessons),
  ]);
  for (const id of ids) {
    const merged = mergeLessonEntry(
      entryAfterReset(left.lessons[id], resetAt),
      entryAfterReset(right.lessons[id], resetAt),
    );
    if (merged) lessons[id] = merged;
  }

  return {
    version: 1,
    currentLessonId:
      newer.currentLessonId || left.currentLessonId || right.currentLessonId,
    updatedAt: later(left.updatedAt, right.updatedAt),
    resetAt,
    lessons,
    practice: mergePractice(left.practice, right.practice),
  };
}

// 题序/断点不按 updatedAt 合并——时间戳一旦被写错（比如写成了未来某个时间），
// 之后任何真实时间都不可能再"更新"，会导致进度永久卡死、来回被坏数据覆盖。
// 改成按内容本身判断：空题序永远不会赢过非空题序，两边都非空时取做得更靠后的
// 那一侧；这样合并结果只看实际进度，不受时间戳异常影响。
function mergePractice(a, b) {
  const chosen =
    a.order.length === 0
      ? b
      : b.order.length === 0
        ? a
        : a.index >= b.index
          ? a
          : b;
  return {
    order: chosen.order,
    index: Math.min(chosen.index, chosen.order.length),
    wrong: { ...a.wrong, ...b.wrong },
  };
}

function entryAfterReset(entry, resetAt) {
  if (!entry || typeof entry !== "object") return null;
  if (resetAt && !((entry.completedAt || "") > resetAt)) return null;
  return entry;
}

function mergeLessonEntry(a, b) {
  if (!a && !b) return null;
  if (!a) return { ...b };
  if (!b) return { ...a };
  const completedAt = later(a.completedAt, b.completedAt);
  // lastTimeMs should reflect whichever attempt actually happened last.
  const mostRecent = completedAt && completedAt === b.completedAt ? b : a;
  return {
    completed: Boolean(a.completed || b.completed),
    attempts: Math.max(a.attempts || 0, b.attempts || 0),
    bestCorrect: Math.max(a.bestCorrect || 0, b.bestCorrect || 0),
    bestPercent: Math.max(a.bestPercent || 0, b.bestPercent || 0),
    bestTimeMs: minPositive(a.bestTimeMs, b.bestTimeMs),
    lastTimeMs: mostRecent.lastTimeMs ?? a.lastTimeMs ?? b.lastTimeMs ?? null,
    total: Math.max(a.total || 0, b.total || 0),
    completedAt,
  };
}

function later(a = "", b = "") {
  return (b || "") > (a || "") ? b : a || "";
}

export function getLessonProgress(progress, lesson) {
  const normalized = normalizeProgress(progress);
  return normalized.lessons[lesson.id] || null;
}

export function getProgressSummary(progress, lessons) {
  const normalized = normalizeProgress(progress);
  const completed = lessons.filter(
    (lesson) => normalized.lessons[lesson.id]?.completed,
  ).length;
  const total = lessons.length;

  return {
    completed,
    total,
    percent: total === 0 ? 0 : Math.round((completed / total) * 100),
  };
}

export function resolveInitialLessonIndex(progress, lessons) {
  const normalized = normalizeProgress(progress);
  const index = lessons.findIndex(
    (lesson) => lesson.id === normalized.currentLessonId,
  );
  return index >= 0 ? index : 0;
}
