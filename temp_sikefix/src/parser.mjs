import fs from "node:fs";
import path from "node:path";

const OPTION_RE = /^-\s+(?:\*\*)?([A-D])\.\s*(.+)$/gm;
const PASSAGE_WORDS = new Map([
  ["1", "One"],
  ["one", "One"],
  ["2", "Two"],
  ["two", "Two"],
]);

export function buildLessons({ sourceRoot, minYear = 2016 }) {
  const manifestPath = path.join(sourceRoot, "manifest.json");
  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
  const zhOverrides = {
    questionZh: loadZhOverrides(sourceRoot, "question-zh.json"),
    answerZh: loadZhOverrides(sourceRoot, "answer-zh.json"),
    lesson: loadZhOverrides(sourceRoot, "lesson-zh.json"),
  };
  const lessons = [];

  for (const entry of manifest) {
    if (Number(entry.year) < minYear) continue;

    const answerPath = path.join(sourceRoot, entry.directory, entry.answerFile);
    if (!fs.existsSync(answerPath)) continue;

    for (const file of entry.files) {
      const passagePath = path.join(sourceRoot, entry.directory, file);
      if (!fs.existsSync(passagePath)) continue;

      try {
        const lesson = parsePassageMarkdown({
          passagePath,
          answerPath,
          examTitle: entry.title,
          examDate: entry.examDate,
          year: entry.year,
        });
        if (lesson.questions.length === 5) {
          lessons.push(applyZhOverrides(lesson, zhOverrides));
        }
      } catch {
        // A malformed source file should not block the whole study deck.
      }
    }
  }

  return lessons.sort((a, b) => a.sortKey.localeCompare(b.sortKey));
}

// 人工校对的中文翻译（sourceRoot/question-zh.json 与 answer-zh.json，键为 `课程id|题号`）。
// 解析器自动生成的 questionZh / answerZh 只是缺失时的兜底。
function loadZhOverrides(sourceRoot, fileName) {
  try {
    const raw = JSON.parse(
      fs.readFileSync(path.join(sourceRoot, fileName), "utf8"),
    );
    return raw && typeof raw === "object" ? raw : {};
  } catch {
    return {};
  }
}

function applyZhOverrides(lesson, overrides) {
  const lessonZh = overrides.lesson[lesson.id] || {};
  return {
    ...lesson,
    ...(lessonZh.mainIdeaZh ? { mainIdeaZh: lessonZh.mainIdeaZh } : {}),
    ...(lessonZh.mainIdeaEn ? { mainIdeaEn: lessonZh.mainIdeaEn } : {}),
    ...(lessonZh.mnemonic ? { answerMnemonic: lessonZh.mnemonic } : {}),
    questions: lesson.questions.map((question) => {
      const key = `${lesson.id}|${question.number}`;
      const next = { ...question };
      if (overrides.questionZh[key]) next.questionZh = overrides.questionZh[key];
      if (overrides.answerZh[key]) next.answerZh = overrides.answerZh[key];
      return next;
    }),
  };
}

export function parsePassageMarkdown({
  passagePath,
  answerPath,
  examTitle,
  examDate,
  year,
}) {
  const passageMarkdown = fs.readFileSync(passagePath, "utf8");
  const answerMarkdown = fs.readFileSync(answerPath, "utf8");
  const title = firstMatch(passageMarkdown, /^#\s+(.+)$/m) || examTitle;
  const examId = firstMatch(passageMarkdown, /^-\s*examId:\s*(\S+)/m) || slug(title);
  const passageLabel = normalizePassageLabel(title, passagePath);
  const passageNumber = passageLabel === "Passage Two" ? 2 : 1;
  const originalText = getSection(passageMarkdown, "原文", "题目");
  const questionsBlock = getSection(passageMarkdown, "题目");
  const answerSection = getAnswerPassageSection(answerMarkdown, passageLabel);
  const translation = getSection(answerSection, "参考翻译", "答案解析");
  const answerMap = parseAnswerMap(answerSection);
  const questions = parseQuestions(questionsBlock).map((question) => {
    const answer = answerMap.get(question.number);
    const answerOption = question.options.find(
      (option) => option.label === answer?.letter,
    );

    return {
      ...question,
      answer: answer?.letter || "",
      answerText: answerOption?.text || "",
      answerZh: makeAnswerZh(answer?.explanation || ""),
      explanation: answer?.explanation || "",
      questionZh: makeQuestionZh(question.stem),
    };
  });
  const answerCode = questions.map((question) => question.answer || "-").join("");

  return {
    id: `${examId}-p${passageNumber}`,
    title,
    examTitle,
    examDate,
    year: String(year),
    passageLabel,
    passageNumber,
    sortKey: makeSortKey({ examId, examDate, title, passageNumber }),
    mainIdeaZh: summarizeChinese(translation),
    mainIdeaEn: summarizeEnglish(originalText),
    answerCode,
    answerMnemonic: makeAnswerMnemonic(questions, answerCode),
    questions,
  };
}

// 兜底的模板式题干翻译；正式翻译来自 question-zh.json 覆盖文件。
// 注意不要从答案解析里抽句子——那描述的是答案含义，会和 answerZh 重复。
export function makeQuestionZh(stem) {
  const normalized = stem.replace(/\s+/g, " ").trim();
  const why = normalized.match(/^Why\s+(.+)\?$/i);
  if (why) return `为什么 ${why[1]}?`;

  const whatDoes = normalized.match(/^What\s+does\s+(.+?)\s+(say|suggest|believe|think|find|mean|show|serve to show)(.*)\?$/i);
  if (whatDoes) return `${capitalizeChineseSubject(whatDoes[1])}${verbZh(whatDoes[2])}${whatDoes[3]}？`;

  const whatDo = normalized.match(/^What\s+do\s+(.+?)\s+(learn|find|believe|suggest)(.*)\?$/i);
  if (whatDo) return `${capitalizeChineseSubject(whatDo[1])}${verbZh(whatDo[2])}${whatDo[3]}？`;

  const how = normalized.match(/^How\s+(.+)\?$/i);
  if (how) return `如何 ${how[1]}?`;

  const what = normalized.match(/^What\s+(.+)\?$/i);
  if (what) return `${what[1]} 是什么？`;

  return `这题考：${normalized}`;
}

export function makeAnswerZh(explanation = "") {
  return extractChineseHint(explanation) || "暂无答案中文意思。";
}

export function makeAnswerMnemonic(questions, answerCode) {
  const steps = ["先", "再", "然后", "接着", "最后"];
  const hooks = questions.map((question, index) => {
    const hook = makeAnswerHook(question.answerZh || question.answerText || "");
    return `${steps[index]}${hook}`;
  });
  return `小剧场：${hooks.join("，")}。`;
}

function firstMatch(text, regex) {
  return text.match(regex)?.[1]?.trim();
}

function getSection(markdown, heading, nextHeading) {
  const startRe = new RegExp(`^#{2,}\\s+${escapeRegExp(heading)}\\s*$`, "m");
  const startMatch = markdown.match(startRe);
  if (!startMatch || startMatch.index === undefined) return "";

  const contentStart = startMatch.index + startMatch[0].length;
  const rest = markdown.slice(contentStart);
  if (!nextHeading) return rest.trim();

  const endRe = new RegExp(`^#{2,}\\s+${escapeRegExp(nextHeading)}\\s*$`, "m");
  const endMatch = rest.match(endRe);
  return (endMatch ? rest.slice(0, endMatch.index) : rest).trim();
}

function getAnswerPassageSection(markdown, targetLabel) {
  const headings = [...markdown.matchAll(/^##\s+(.+)$/gm)];
  for (let index = 0; index < headings.length; index += 1) {
    const heading = headings[index];
    const label = normalizePassageLabel(heading[1], "");
    if (label !== targetLabel || heading.index === undefined) continue;

    const next = headings[index + 1];
    return markdown.slice(
      heading.index,
      next?.index ?? markdown.length,
    );
  }

  return markdown;
}

function parseAnswerMap(markdown) {
  const answers = new Map();
  const answerRe = /^###\s*(\d+)\.\s*(.*?)\n-\s*答案：\s*([A-D])\s*\n-\s*解析：\s*([\s\S]*?)(?=^###\s*\d+\.|^##\s+|(?![\s\S]))/gm;
  for (const match of markdown.matchAll(answerRe)) {
    answers.set(match[1], {
      stem: clean(match[2]),
      letter: match[3],
      explanation: clean(match[4]),
    });
  }
  return answers;
}

function parseQuestions(markdown) {
  const questionRe = /^###\s*(\d+)\.\s*(.*?)\n([\s\S]*?)(?=^###\s*\d+\.|(?![\s\S]))/gm;
  const questions = [];

  for (const match of markdown.matchAll(questionRe)) {
    const options = [];
    for (const option of match[3].matchAll(OPTION_RE)) {
      options.push({
        label: option[1],
        text: cleanMarkdown(option[2]),
      });
    }

    questions.push({
      number: match[1],
      stem: clean(match[2]),
      options,
    });
  }

  return questions;
}

function normalizePassageLabel(value, filePath) {
  const text = `${value} ${filePath}`.toLowerCase();
  const match = text.match(/passage[\s-]*(one|two|1|2)/);
  const word = PASSAGE_WORDS.get(match?.[1] || "1") || "One";
  return `Passage ${word}`;
}

function summarizeChinese(text) {
  const cleanText = clean(text);
  if (!cleanText) return "暂无中文大意。";
  return takeSentences(cleanText, /[。！？]/, 3, 150);
}

function summarizeEnglish(text) {
  const cleanText = clean(text);
  if (!cleanText) return "No English gist is available.";
  return takeSentences(cleanText, /(?<=[.!?])\s+/, 3, 260);
}

function takeSentences(text, splitter, maxSentences, maxChars) {
  const sentences = text
    .split(splitter)
    .map((sentence) => sentence.trim())
    .filter(Boolean);
  const joined = sentences.slice(0, maxSentences).join(" ");
  return truncate(joined || text, maxChars);
}

function extractChineseHint(explanation) {
  const plain = clean(explanation)
    .replace(/'[^']+'/g, "")
    .replace(/"[^"]+"/g, "");
  if (!plain) return "";

  const sentences = plain
    .split(/[。！？]/)
    .map((sentence) => sentence.trim())
    .filter(Boolean);
  const useful = sentences.find((sentence) =>
    !/^这是一道/.test(sentence) &&
    /(意味着|表明|说明|强调|指出|认为|暗示|可知|提到|显示|反映|原因|建议|需要)/.test(sentence),
  ) || sentences.find((sentence) => !/^这是一道/.test(sentence) && sentence.length > 8);

  if (!useful) return "";

  const conclusion = useful.match(/(?:意味着|表明|说明|显示|反映|暗示|可知)(.+)$/);
  const concise = conclusion?.[1] && /[\u4e00-\u9fff]/.test(conclusion[1])
    ? conclusion[1]
    : useful;

  return truncate(
    concise
      .replace(/^这(表明|说明|强调)/, "这题考")
      .replace(/因此.*$/, "")
      .replace(/所以.*$/, "")
      .replace(/，?故.*$/, "")
      .replace(/^[，、。；：,;:\s]+/, "")
      .trim(),
    72,
  );
}

function capitalizeChineseSubject(subject) {
  const normalized = subject.trim();
  const subjects = new Map([
    ["the author", "作者"],
    ["the authors", "作者"],
    ["the passage", "文章"],
    ["we", "我们"],
  ]);
  return subjects.get(normalized.toLowerCase()) || normalized;
}

function verbZh(verb) {
  const verbs = new Map([
    ["say", "说了什么"],
    ["suggest", "建议什么"],
    ["believe", "认为"],
    ["think", "认为"],
    ["find", "发现"],
    ["mean", "意思是"],
    ["show", "说明"],
    ["serve to show", "用来说明"],
    ["learn", "了解到"],
  ]);
  return verbs.get(verb.toLowerCase()) || "考察";
}

function makeSortKey({ examId, examDate, title, passageNumber }) {
  const source = `${examId} ${examDate} ${title}`;
  const year = source.match(/20\d{2}/)?.[0] || "9999";
  const month = source.match(/(\d{2})月/)?.[1] || "99";
  const suite = source.match(/第(\d+)套/)?.[1]?.padStart(2, "0") || "99";
  return `${year}-${month}-${suite}-${String(passageNumber).padStart(2, "0")}`;
}

function clean(text) {
  return text.replace(/\r/g, "").replace(/\s+/g, " ").trim();
}

function cleanMarkdown(text) {
  return clean(text).replace(/\*\*$/g, "").replace(/\*\*/g, "").trim();
}

function truncate(text, maxChars) {
  if (text.length <= maxChars) return text;
  return `${text.slice(0, maxChars - 1).trim()}…`;
}

// 兜底的口诀片段提取；正式口诀来自 lesson-zh.json 覆盖文件。
// 不要按主题词硬编码口语短语——那些短语只适用于个别文章，跨课匹配会张冠李戴。
function makeAnswerHook(value) {
  const cleaned = clean(value)
    .replace(/^这题考[:：]?/, "")
    .replace(/^答案中文[:：]?/, "");

  const contrast = cleaned.match(/但实际上(.+)$/);
  if (contrast?.[1]) return truncate(polishHook(contrast[1]), 18);

  const sentence = cleaned.split(/[，。；;]/).find((part) => part.trim().length >= 4) || cleaned;
  return truncate(polishHook(sentence), 18);
}

function polishHook(value) {
  return value
    .replace(/^文中提到/, "")
    .replace(/^文章提到/, "")
    .replace(/^作者认为/, "")
    .replace(/^这说明/, "")
    .replace(/^这表明/, "")
    .replace(/^并/, "")
    .trim();
}

function slug(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
