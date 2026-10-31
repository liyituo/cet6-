import assert from "node:assert/strict";
import { describe, it } from "node:test";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  buildLessons,
  makeQuestionZh,
  parsePassageMarkdown,
} from "../src/parser.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "../..");

describe("parsePassageMarkdown", () => {
  it("extracts a passage, five questions, options, and answers from CET6 markdown", () => {
    const lesson = parsePassageMarkdown({
      passagePath: path.join(
        repoRoot,
        "sectionc_readings/2018/12月_第1套/passage-one.md",
      ),
      answerPath: path.join(
        repoRoot,
        "sectionc_readings/2018/12月_第1套/答案解析与翻译.md",
      ),
      examTitle: "CET6 2018年12月 第1套",
      examDate: "2018年12月",
      year: "2018",
    });

    assert.equal(lesson.title, "CET6 2018年12月 第1套 · Passage One");
    assert.equal(lesson.questions.length, 5);
    assert.equal(lesson.questions[0].number, "46");
    assert.equal(lesson.questions[0].answer, "B");
    assert.equal(lesson.questions[0].options.length, 4);
    assert.match(lesson.mainIdeaZh, /机器人|农民/);
    assert.match(lesson.mainIdeaEn, /robots|farmers/i);
    assert.ok(lesson.questions[0].questionZh.length > 6);
  });

  it("keeps bolded correct options as normal answer choices", () => {
    const lesson = parsePassageMarkdown({
      passagePath: path.join(
        repoRoot,
        "sectionc_readings/2016/06月_第1套/passage-one.md",
      ),
      answerPath: path.join(
        repoRoot,
        "sectionc_readings/2016/06月_第1套/答案解析与翻译.md",
      ),
      examTitle: "CET6 2016年06月 第1套",
      examDate: "2016年06月",
      year: "2016",
    });

    assert.equal(lesson.questions[0].options.length, 4);
    assert.equal(lesson.questions[0].answer, "D");
    assert.equal(
      lesson.questions[0].answerText,
      "Interactive television advertising has not achieved the anticipated results.",
    );
    assert.match(lesson.questions[0].answerZh, /没有达到预期|预期的效果/);
    assert.doesNotMatch(lesson.questions[0].answerZh, /词义猜测题/);
    assert.equal(lesson.answerCode.length, 5);
    assert.doesNotMatch(lesson.answerMnemonic, new RegExp(`^${lesson.answerCode}`));
    assert.match(lesson.answerMnemonic, /小剧场|先|最后/);
    assert.match(lesson.answerMnemonic, /预期|怀疑|吃亏|新鲜/);
  });

  it("builds all available lessons from manifest entries after 2016", () => {
    const lessons = buildLessons({
      sourceRoot: path.join(repoRoot, "sectionc_readings"),
      minYear: 2016,
    });

    assert.ok(lessons.length >= 40);
    assert.ok(lessons.every((lesson) => Number(lesson.year) >= 2016));
    assert.ok(lessons.every((lesson) => lesson.questions.length === 5));
  });
});

describe("makeQuestionZh", () => {
  it("falls back to a Chinese question prompt when no explanation is available", () => {
    assert.equal(
      makeQuestionZh("Why are farmers pressing for robotic farming?", ""),
      "为什么 are farmers pressing for robotic farming?",
    );
  });
});
