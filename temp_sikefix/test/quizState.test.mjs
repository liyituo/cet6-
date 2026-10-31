import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { answerCurrent, createQuiz, getResult } from "../src/quizState.mjs";

const lesson = {
  id: "demo",
  questions: [
    {
      number: "46",
      answer: "B",
      stem: "What does the passage mainly discuss?",
      options: [
        { label: "A", text: "A wrong idea." },
        { label: "B", text: "The right idea." },
      ],
    },
    {
      number: "47",
      answer: "A",
      stem: "What does the author suggest?",
      options: [
        { label: "A", text: "Act now." },
        { label: "B", text: "Wait longer." },
      ],
    },
  ],
};

describe("quizState", () => {
  it("records answers and advances through a lesson", () => {
    let quiz = createQuiz(lesson);

    quiz = answerCurrent(quiz, "B");
    assert.equal(quiz.currentIndex, 1);
    assert.equal(quiz.answers[0].isCorrect, true);
    assert.equal(quiz.answers[0].correctText, "The right idea.");

    quiz = answerCurrent(quiz, "B");
    assert.equal(quiz.isComplete, true);
    assert.deepEqual(getResult(quiz), {
      correct: 1,
      total: 2,
      percent: 50,
    });
  });

  it("rejects answers after a quiz is complete", () => {
    let quiz = createQuiz(lesson);
    quiz = answerCurrent(answerCurrent(quiz, "B"), "A");

    assert.throws(() => answerCurrent(quiz, "A"), /complete/);
  });
});
