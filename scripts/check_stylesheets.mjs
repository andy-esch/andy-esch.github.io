#!/usr/bin/env node
/**
 * Validate generated stylesheets against the CSS specifications.
 *
 * `scripts/check_generated_site.py` already proves every `url()` in the output
 * resolves to a real local file. This adds the standards-level half: csstree
 * parses each stylesheet and checks declarations against the W3C/MDN property
 * value definitions, so an unknown property or a malformed value fails the gate.
 *
 * Makes no network requests.
 */

import { globSync, readFileSync } from "node:fs";
import { relative, resolve } from "node:path";
import { validate } from "csstree-validator";

const siteDir = resolve(process.argv[2] ?? "public");
const stylesheets = globSync("**/*.css", { cwd: siteDir })
  .map((name) => resolve(siteDir, name))
  .sort();

if (stylesheets.length === 0) {
  console.error(`no stylesheets found in ${siteDir}`);
  process.exit(1);
}

const problems = [];

for (const path of stylesheets) {
  const css = readFileSync(path, "utf8");
  for (const error of validate(css, path)) {
    const where = error.line ? `:${error.line}:${error.column ?? 1}` : "";
    const detail = error.property ? ` (${error.property})` : "";
    problems.push(
      `${relative(siteDir, path)}${where}: ${error.name ?? "CssSyntaxError"}: ` +
        `${error.message ?? String(error)}${detail}`,
    );
  }
}

if (problems.length > 0) {
  console.error("stylesheet validation failed:");
  for (const problem of problems) {
    console.error(`- ${problem}`);
  }
  process.exit(1);
}

console.log(`validated ${stylesheets.length} stylesheet(s) against CSS specifications`);
