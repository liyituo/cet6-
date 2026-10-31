import assert from "node:assert/strict";
import { after, before, describe, it } from "node:test";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { createAppServer } from "../server.mjs";

describe("progress API server", () => {
  const dataFile = path.join(
    fs.mkdtempSync(path.join(os.tmpdir(), "cet6-sync-")),
    "progress.json",
  );
  const server = createAppServer({ dataFile });
  let base = "";

  before(async () => {
    await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
    base = `http://127.0.0.1:${server.address().port}`;
  });

  after(() => server.close());

  it("serves the app shell", async () => {
    const response = await fetch(`${base}/`);
    assert.equal(response.status, 200);
    assert.match(await response.text(), /六级 Section C 原题速记/);
  });

  it("returns empty progress before any sync", async () => {
    const response = await fetch(`${base}/api/progress`);
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.currentLessonId, "");
    assert.deepEqual(body.lessons, {});
  });

  it("merges progress from two devices instead of overwriting", async () => {
    const deviceA = {
      version: 1,
      currentLessonId: "p1",
      updatedAt: "2026-07-02T10:00:00.000Z",
      resetAt: "",
      lessons: {
        p1: {
          completed: true,
          attempts: 1,
          bestCorrect: 3,
          bestPercent: 60,
          total: 5,
          completedAt: "2026-07-02T10:00:00.000Z",
        },
      },
    };
    const deviceB = {
      version: 1,
      currentLessonId: "p2",
      updatedAt: "2026-07-03T10:00:00.000Z",
      resetAt: "",
      lessons: {
        p1: {
          completed: true,
          attempts: 2,
          bestCorrect: 5,
          bestPercent: 100,
          total: 5,
          completedAt: "2026-07-03T09:00:00.000Z",
        },
        p2: {
          completed: true,
          attempts: 1,
          bestCorrect: 4,
          bestPercent: 80,
          total: 5,
          completedAt: "2026-07-03T09:30:00.000Z",
        },
      },
    };

    const putA = await fetch(`${base}/api/progress`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(deviceA),
    });
    assert.equal(putA.status, 200);

    const putB = await fetch(`${base}/api/progress`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(deviceB),
    });
    const merged = await putB.json();
    assert.equal(merged.currentLessonId, "p2");
    assert.equal(merged.lessons.p1.bestCorrect, 5);
    assert.equal(merged.lessons.p2.bestCorrect, 4);

    // 设备 A 再次提交旧数据也不会把 B 的进度冲掉
    const replay = await fetch(`${base}/api/progress`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(deviceA),
    });
    const afterReplay = await replay.json();
    assert.equal(afterReplay.currentLessonId, "p2");
    assert.equal(afterReplay.lessons.p2.bestCorrect, 4);

    const stored = JSON.parse(fs.readFileSync(dataFile, "utf8"));
    assert.equal(stored.lessons.p1.bestCorrect, 5);
  });

  it("rejects invalid JSON payloads", async () => {
    const response = await fetch(`${base}/api/progress`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: "not-json{",
    });
    assert.equal(response.status, 400);
  });

  it("blocks path traversal outside the app root", async () => {
    const response = await fetch(`${base}/..%2F..%2Fetc%2Fpasswd`);
    assert.equal(response.status, 404);
  });
});
