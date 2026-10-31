import assert from "node:assert/strict";
import { describe, it } from "node:test";

import {
  clearPracticeWrong,
  createEmptyProgress,
  getProgressSummary,
  markLessonComplete,
  markPracticeWrong,
  mergeProgress,
  normalizeProgress,
  resetAllProgress,
  resolveInitialLessonIndex,
  savePracticeRun,
} from "../src/progressStore.mjs";

const lessons = [
  { id: "p1", title: "Passage 1" },
  { id: "p2", title: "Passage 2" },
];

describe("progressStore", () => {
  it("tracks attempts, completion, and best score per lesson", () => {
    let progress = createEmptyProgress();

    progress = markLessonComplete(progress, lessons[0], {
      correct: 3,
      total: 5,
      percent: 60,
    });
    progress = markLessonComplete(progress, lessons[0], {
      correct: 2,
      total: 5,
      percent: 40,
    });

    assert.equal(progress.lessons.p1.completed, true);
    assert.equal(progress.lessons.p1.attempts, 2);
    assert.equal(progress.lessons.p1.bestCorrect, 3);
    assert.equal(progress.lessons.p1.bestPercent, 60);
  });

  it("tracks the fastest and most recent time per lesson", () => {
    let progress = createEmptyProgress();

    progress = markLessonComplete(
      progress,
      lessons[0],
      { correct: 5, total: 5, percent: 100 },
      90_000,
    );
    progress = markLessonComplete(
      progress,
      lessons[0],
      { correct: 4, total: 5, percent: 80 },
      60_000,
    );
    progress = markLessonComplete(
      progress,
      lessons[0],
      { correct: 5, total: 5, percent: 100 },
      75_000,
    );

    assert.equal(progress.lessons.p1.bestTimeMs, 60_000);
    assert.equal(progress.lessons.p1.lastTimeMs, 75_000);
  });

  it("ignores a missing/invalid time instead of recording garbage", () => {
    let progress = createEmptyProgress();
    progress = markLessonComplete(progress, lessons[0], { correct: 5, total: 5, percent: 100 });
    assert.equal(progress.lessons.p1.bestTimeMs, null);
    assert.equal(progress.lessons.p1.lastTimeMs, null);

    progress = markLessonComplete(
      progress,
      lessons[0],
      { correct: 5, total: 5, percent: 100 },
      -5,
    );
    assert.equal(progress.lessons.p1.bestTimeMs, null);
  });

  it("summarizes completed lessons and resumes the saved lesson index", () => {
    let progress = createEmptyProgress();
    progress.currentLessonId = "p2";
    progress = markLessonComplete(progress, lessons[0], {
      correct: 5,
      total: 5,
      percent: 100,
    });

    assert.deepEqual(getProgressSummary(progress, lessons), {
      completed: 1,
      total: 2,
      percent: 50,
    });
    assert.equal(resolveInitialLessonIndex(progress, lessons), 1);
  });
});

describe("mergeProgress", () => {
  const entry = (overrides) => ({
    completed: true,
    attempts: 1,
    bestCorrect: 3,
    bestPercent: 60,
    total: 5,
    completedAt: "2026-07-01T10:00:00.000Z",
    ...overrides,
  });

  it("unions lessons and keeps the best score per lesson", () => {
    const deviceA = {
      version: 1,
      currentLessonId: "p1",
      updatedAt: "2026-07-02T10:00:00.000Z",
      resetAt: "",
      lessons: { p1: entry({ bestCorrect: 3, bestPercent: 60 }) },
    };
    const deviceB = {
      version: 1,
      currentLessonId: "p2",
      updatedAt: "2026-07-03T10:00:00.000Z",
      resetAt: "",
      lessons: {
        p1: entry({ bestCorrect: 5, bestPercent: 100, attempts: 2 }),
        p2: entry({ completedAt: "2026-07-03T09:00:00.000Z" }),
      },
    };

    const merged = mergeProgress(deviceA, deviceB);
    assert.deepEqual(Object.keys(merged.lessons).sort(), ["p1", "p2"]);
    assert.equal(merged.lessons.p1.bestCorrect, 5);
    assert.equal(merged.lessons.p1.bestPercent, 100);
    assert.equal(merged.lessons.p1.attempts, 2);
  });

  it("takes currentLessonId from the side updated most recently", () => {
    const older = {
      version: 1,
      currentLessonId: "p1",
      updatedAt: "2026-07-02T10:00:00.000Z",
      resetAt: "",
      lessons: {},
    };
    const newer = {
      version: 1,
      currentLessonId: "p2",
      updatedAt: "2026-07-03T10:00:00.000Z",
      resetAt: "",
      lessons: {},
    };

    assert.equal(mergeProgress(older, newer).currentLessonId, "p2");
    assert.equal(mergeProgress(newer, older).currentLessonId, "p2");
    assert.equal(
      mergeProgress(older, newer).updatedAt,
      "2026-07-03T10:00:00.000Z",
    );
  });

  it("drops lessons completed before the latest reset, keeps ones after", () => {
    const resetSide = resetAllProgress({ id: "p1" });
    const otherSide = {
      version: 1,
      currentLessonId: "p2",
      updatedAt: "2026-07-01T10:00:00.000Z",
      resetAt: "",
      lessons: {
        p1: entry({ completedAt: "2026-07-01T09:00:00.000Z" }),
      },
    };

    const merged = mergeProgress(otherSide, resetSide);
    assert.deepEqual(merged.lessons, {});
    assert.equal(merged.resetAt, resetSide.resetAt);

    // 重置之后（时间戳严格晚于 resetAt）完成的记录要保留
    const afterReset = {
      version: 1,
      currentLessonId: "p2",
      updatedAt: "2099-01-01T00:00:00.000Z",
      resetAt: merged.resetAt,
      lessons: {
        p2: entry({
          bestCorrect: 4,
          bestPercent: 80,
          completedAt: "2099-01-01T00:00:00.000Z",
        }),
      },
    };
    const remerged = mergeProgress(afterReset, resetSide);
    assert.equal(remerged.lessons.p2.bestCorrect, 4);
  });

  it("is idempotent when merging identical progress", () => {
    let progress = markLessonComplete(createEmptyProgress(), lessons[0], {
      correct: 5,
      total: 5,
      percent: 100,
    });
    assert.deepEqual(mergeProgress(progress, progress), {
      ...progress,
      version: 1,
    });
  });

  it("never lets an empty practice order win over a real one, even with a bogus future updatedAt", () => {
    // Regression test: practice merging used to pick the side with the
    // newer `updatedAt` wholesale. A single corrupted/future timestamp
    // (e.g. accidentally set to year 2099) could never be beaten by any
    // real date again, permanently reverting practice progress on every
    // sync. It must now be decided by content (order length / index),
    // not by the timestamp.
    const realRun = savePracticeRun(createEmptyProgress(), ["a", "b", "c"], 2);
    const corrupted = {
      ...createEmptyProgress(),
      updatedAt: "2099-01-01T00:00:00.000Z",
    };

    assert.deepEqual(mergeProgress(realRun, corrupted).practice, realRun.practice);
    assert.deepEqual(mergeProgress(corrupted, realRun).practice, realRun.practice);
  });

  it("prefers whichever non-empty practice run has progressed further", () => {
    const behind = savePracticeRun(createEmptyProgress(), ["a", "b", "c"], 1);
    const ahead = savePracticeRun(createEmptyProgress(), ["a", "b", "c"], 2);

    assert.equal(mergeProgress(behind, ahead).practice.index, 2);
    assert.equal(mergeProgress(ahead, behind).practice.index, 2);
  });

  it("unions the wrong-question list regardless of which side's order wins", () => {
    let a = savePracticeRun(createEmptyProgress(), ["a", "b", "c"], 2);
    a = markPracticeWrong(a, "p1::46");
    let b = savePracticeRun(createEmptyProgress(), ["a", "b", "c"], 1);
    b = markPracticeWrong(b, "p2::51");

    const merged = mergeProgress(a, b);
    assert.deepEqual(Object.keys(merged.practice.wrong).sort(), ["p1::46", "p2::51"]);
  });

  it("keeps the fastest time across devices and the most recently-run attempt's time", () => {
    let slowerButEarlier = markLessonComplete(
      createEmptyProgress(),
      lessons[0],
      { correct: 5, total: 5, percent: 100 },
      90_000,
    );
    let fasterButLater = markLessonComplete(
      createEmptyProgress(),
      lessons[0],
      { correct: 5, total: 5, percent: 100 },
      60_000,
    );
    // Force explicit, unambiguous completedAt on both sides so "most
    // recent" doesn't depend on real wall-clock timing during the test.
    slowerButEarlier = {
      ...slowerButEarlier,
      lessons: { p1: { ...slowerButEarlier.lessons.p1, completedAt: "2026-07-01T10:00:00.000Z" } },
    };
    fasterButLater = {
      ...fasterButLater,
      lessons: { p1: { ...fasterButLater.lessons.p1, completedAt: "2026-07-02T10:00:00.000Z" } },
    };

    const merged = mergeProgress(slowerButEarlier, fasterButLater);
    assert.equal(merged.lessons.p1.bestTimeMs, 60_000);
    assert.equal(merged.lessons.p1.lastTimeMs, 60_000);
  });
});

describe("practice run tracking", () => {
  it("persists the shuffled run order and current position", () => {
    let progress = createEmptyProgress();
    progress = savePracticeRun(progress, ["p1::46", "p2::46"], 1);

    assert.deepEqual(progress.practice.order, ["p1::46", "p2::46"]);
    assert.equal(progress.practice.index, 1);
  });

  it("records a wrong answer and clears it once corrected", () => {
    let progress = createEmptyProgress();
    progress = markPracticeWrong(progress, "p1::46");
    assert.equal(progress.practice.wrong["p1::46"], true);

    progress = markPracticeWrong(progress, "p2::51");
    assert.deepEqual(Object.keys(progress.practice.wrong).sort(), ["p1::46", "p2::51"]);

    progress = clearPracticeWrong(progress, "p1::46");
    assert.deepEqual(Object.keys(progress.practice.wrong), ["p2::51"]);
  });

  it("normalizes a missing/malformed practice field to safe defaults", () => {
    assert.deepEqual(createEmptyProgress().practice, { order: [], index: 0, wrong: {} });
    const normalized = normalizeProgress({
      practice: { order: "not-an-array", index: -5, wrong: null },
    });
    assert.deepEqual(normalized.practice, { order: [], index: 0, wrong: {} });
  });
});
