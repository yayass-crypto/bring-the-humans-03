// bring-the-humans-03 — the program for this entry (Node 22, standard library only).
//
// The entry itself is the video: an original short vertical ad for make.fun,
// made by my AI agent in its build session, posted publicly on TikTok, and
// named here in VIDEO.json. All this program has to do is hand that file to
// the grader: it reads VIDEO.json from the repository root, checks it is a
// JSON object with a string "url", and copies it to the output directory,
// where the house reads the video's views from TikTok. Nothing this program
// writes about the video is scored — the house reads the video itself.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// It prints nothing on success. Outside the grader's container the two
// environment variables stand in for /bot and /output.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(BOT_DIR, "VIDEO.json");
const target = join(OUTPUT_DIR, "VIDEO.json");

let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(source, "utf8"));
} catch (err) {
  console.error(`VIDEO.json could not be read from ${source}: ${(err as Error).message}`);
  process.exit(1);
}

if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string" ||
  ((parsed as { url: string }).url.length === 0)
) {
  console.error(`VIDEO.json in ${source} is not {"url": "<TikTok video address>"}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(source, target);
} catch (err) {
  console.error(`VIDEO.json could not be copied to ${target}: ${(err as Error).message}`);
  process.exit(1);
}
