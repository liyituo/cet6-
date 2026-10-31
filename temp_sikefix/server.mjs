import fs from "node:fs";
import fsp from "node:fs/promises";
import http from "node:http";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  createEmptyProgress,
  mergeProgress,
  normalizeProgress,
} from "./src/progressStore.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const MAX_BODY_BYTES = 1024 * 1024;
const MIME = new Map([
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".mjs", "text/javascript; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".png", "image/png"],
  [".ico", "image/x-icon"],
  [".md", "text/markdown; charset=utf-8"],
]);

export function createAppServer({
  rootDir = __dirname,
  dataFile = path.join(__dirname, "data", "progress.json"),
} = {}) {
  const root = path.resolve(rootDir);
  let writeQueue = Promise.resolve();

  async function readProgress() {
    try {
      return normalizeProgress(JSON.parse(await fsp.readFile(dataFile, "utf8")));
    } catch {
      return createEmptyProgress();
    }
  }

  // 串行化“读-合并-写”，避免两台设备同时提交时丢更新；写入走临时文件+rename 保证原子性。
  function updateProgress(mutate) {
    const task = writeQueue.then(async () => {
      const next = mutate(await readProgress());
      await fsp.mkdir(path.dirname(dataFile), { recursive: true });
      const tmp = `${dataFile}.tmp`;
      await fsp.writeFile(tmp, `${JSON.stringify(next, null, 2)}\n`, "utf8");
      await fsp.rename(tmp, dataFile);
      return next;
    });
    writeQueue = task.catch(() => {});
    return task;
  }

  async function handleProgress(req, res) {
    if (req.method === "GET") {
      sendJson(res, 200, await readProgress());
      return;
    }
    if (req.method === "PUT" || req.method === "POST") {
      let incoming;
      try {
        incoming = JSON.parse(await readBody(req, MAX_BODY_BYTES));
      } catch (error) {
        sendJson(res, 400, { error: `bad request: ${error.message}` });
        return;
      }
      const merged = await updateProgress((stored) =>
        mergeProgress(stored, incoming),
      );
      sendJson(res, 200, merged);
      return;
    }
    res.writeHead(405, { Allow: "GET, PUT, POST" });
    res.end();
  }

  async function serveStatic(req, res, pathname) {
    let rel;
    try {
      rel = decodeURIComponent(pathname);
    } catch {
      sendText(res, 400, "Bad Request");
      return;
    }
    if (rel === "/") rel = "/index.html";
    if (rel.split("/").some((part) => part.startsWith("."))) {
      sendText(res, 404, "Not Found");
      return;
    }

    const filePath = path.normalize(path.join(root, rel));
    if (filePath !== root && !filePath.startsWith(root + path.sep)) {
      sendText(res, 404, "Not Found");
      return;
    }

    let stat;
    try {
      stat = await fsp.stat(filePath);
    } catch {
      sendText(res, 404, "Not Found");
      return;
    }
    if (!stat.isFile()) {
      sendText(res, 404, "Not Found");
      return;
    }

    res.writeHead(200, {
      "Content-Type": MIME.get(path.extname(filePath).toLowerCase()) || "application/octet-stream",
      "Content-Length": stat.size,
      "Cache-Control": "no-store",
    });
    if (req.method === "HEAD") {
      res.end();
      return;
    }
    fs.createReadStream(filePath).pipe(res);
  }

  return http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, "http://localhost");
      if (url.pathname === "/api/progress") {
        await handleProgress(req, res);
        return;
      }
      if (req.method !== "GET" && req.method !== "HEAD") {
        res.writeHead(405, { Allow: "GET, HEAD" });
        res.end();
        return;
      }
      await serveStatic(req, res, url.pathname);
    } catch (error) {
      if (!res.headersSent) sendText(res, 500, `Server error: ${error.message}`);
      else res.end();
    }
  });
}

function readBody(req, limit) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on("data", (chunk) => {
      size += chunk.length;
      if (size > limit) {
        reject(new Error("payload too large"));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}

function sendJson(res, status, value) {
  const body = JSON.stringify(value);
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
  });
  res.end(body);
}

function sendText(res, status, text) {
  res.writeHead(status, { "Content-Type": "text/plain; charset=utf-8" });
  res.end(text);
}

function listUrls(port) {
  const urls = new Set([`http://127.0.0.1:${port}/`]);
  for (const infos of Object.values(os.networkInterfaces())) {
    for (const info of infos || []) {
      if (info.family === "IPv4" && !info.internal) {
        urls.add(`http://${info.address}:${port}/`);
      }
    }
  }
  return [...urls];
}

const isMain =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  const port = Number(process.env.PORT || 4173);
  createAppServer().listen(port, "0.0.0.0", () => {
    console.log("六级速记 server 已启动，进度存储于 data/progress.json：");
    for (const url of listUrls(port)) console.log(`  ${url}`);
  });
}
