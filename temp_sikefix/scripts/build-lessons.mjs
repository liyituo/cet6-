import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildLessons } from "../src/parser.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const appRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(appRoot, "..");
const sourceRoot = path.join(repoRoot, "sectionc_readings");
const outputDir = path.join(appRoot, "public");
const outputPath = path.join(outputDir, "lessons-data.js");

const lessons = buildLessons({ sourceRoot, minYear: 2016 });

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(
  outputPath,
  `window.CET6_LESSONS = ${JSON.stringify(lessons)};\n`,
  "utf8",
);

const kb = Math.round(fs.statSync(outputPath).size / 1024);
console.log(`Wrote ${lessons.length} lessons to ${path.relative(appRoot, outputPath)} (${kb}KB)`);
