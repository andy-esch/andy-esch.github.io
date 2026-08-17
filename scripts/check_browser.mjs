#!/usr/bin/env node
/**
 * Browser-based gates for the generated artifact: an accessibility smoke check
 * and a horizontal-overflow regression check.
 *
 * Every generated HTML document is served from a local ephemeral-port static
 * server and loaded in headless Chromium at each viewport in VIEWPORTS. Per
 * page and viewport it asserts:
 *
 *   1. axe-core reports no WCAG 2.0/2.1 A or AA violations.
 *   2. The document does not scroll horizontally, and the page reports which
 *      elements overflow when it does.
 *
 * Routes are discovered from the artifact rather than hard-coded, so a new page
 * template is covered the moment it is built. Makes no external requests: the
 * server only reads files under the site directory, and axe-core is bundled.
 */

import { createServer } from "node:http";
import { createReadStream, existsSync, globSync, statSync } from "node:fs";
import { extname, join, relative, resolve, sep } from "node:path";
import { chromium } from "playwright";
import { AxeBuilder } from "@axe-core/playwright";

const VIEWPORTS = [
  { name: "mobile", width: 320, height: 640 },
  { name: "tablet", width: 768, height: 1024 },
  { name: "desktop", width: 1280, height: 800 },
];

const AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

/**
 * Per-route page-weight budget, in bytes of uncompressed artifact.
 *
 * The heaviest route currently serves about 93 KiB, nearly all of it the two
 * WOFF2 faces. The ceiling leaves room for real content growth while still
 * catching a regression that matters: reverting the fonts to TTF alone would
 * push the archive route past 200 KiB. GitHub Pages compresses HTML, CSS, and
 * SVG on the wire and WOFF2 is already compressed, so a passing number here is
 * strictly pessimistic against what visitors actually download.
 */
const PAGE_WEIGHT_BUDGET = 150 * 1024;

const WEBFONT_FAMILY = "Archivo";

const CONTENT_TYPES = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".ico": "image/x-icon",
  ".jpg": "image/jpeg",
  ".js": "text/javascript; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
};

/**
 * Serve the artifact read-only, refusing any path that escapes the site root.
 *
 * The server also tallies the bytes it hands out. Counting here rather than in
 * the browser keeps the number deterministic — it is exactly what the artifact
 * would put on the wire, with no cache or protocol overhead mixed in.
 */
function startServer(siteDir) {
  const meter = { bytes: 0 };

  const server = createServer((request, response) => {
    const requestPath = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
    let target = resolve(join(siteDir, requestPath));

    if (target !== siteDir && !target.startsWith(siteDir + sep)) {
      response.writeHead(403).end("forbidden");
      return;
    }
    if (existsSync(target) && statSync(target).isDirectory()) {
      target = join(target, "index.html");
    }
    if (!existsSync(target)) {
      response.writeHead(404).end("not found");
      return;
    }

    meter.bytes += statSync(target).size;
    response.writeHead(200, {
      "content-type": CONTENT_TYPES[extname(target).toLowerCase()] ?? "application/octet-stream",
    });
    createReadStream(target).pipe(response);
  });

  return new Promise((resolveServer) => {
    server.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      resolveServer({ server, origin: `http://127.0.0.1:${port}`, meter });
    });
  });
}

/**
 * Confirm the webfont actually loaded and is what the page renders with.
 *
 * Without this a corrupt or misreferenced font file is invisible: the browser
 * silently falls back to the next family in the stack, every other check still
 * passes, and the site quietly ships in Helvetica.
 */
async function fontProblems(page) {
  return page.evaluate(async (family) => {
    await document.fonts.ready;
    const problems = [];
    // Chromium normalizes FontFace.family to lowercase and may keep the quotes
    // from the stylesheet, so neither case nor quoting can be relied on here.
    const wanted = family.replace(/"/g, "").toLowerCase();
    const loaded = [...document.fonts].filter(
      (face) => face.family.replace(/"/g, "").toLowerCase() === wanted,
    );

    if (loaded.length === 0) {
      problems.push(`no @font-face for ${family} reached the browser`);
      return problems;
    }
    for (const face of loaded) {
      if (face.status !== "loaded") {
        problems.push(`${family} ${face.weight} failed to load (status: ${face.status})`);
      }
    }
    for (const weight of ["400", "700"]) {
      if (!document.fonts.check(`${weight} 1rem "${family}"`)) {
        problems.push(`${family} ${weight} is not usable for rendering`);
      }
    }
    return problems;
  }, WEBFONT_FAMILY);
}

function routesFor(siteDir) {
  return globSync("**/*.html", { cwd: siteDir })
    .map((name) => {
      const path = name.split(sep).join("/");
      if (path === "index.html") return "/";
      return path.endsWith("/index.html") ? `/${path.slice(0, -"index.html".length)}` : `/${path}`;
    })
    .sort();
}

/** Report elements wider than the viewport, which is what makes a page pan sideways. */
async function overflowingElements(page) {
  return page.evaluate(() => {
    const limit = document.documentElement.clientWidth;
    // Sub-pixel layout rounding can exceed the viewport by a hair without being visible.
    const tolerance = 1;
    if (document.documentElement.scrollWidth <= limit + tolerance) return [];

    return [...document.querySelectorAll("body *")]
      .filter((element) => {
        const box = element.getBoundingClientRect();
        return box.width > 0 && box.right > limit + tolerance;
      })
      .slice(0, 5)
      .map((element) => {
        const box = element.getBoundingClientRect();
        const classes = element.className
          ? `.${String(element.className).trim().split(/\s+/).join(".")}`
          : "";
        return `<${element.tagName.toLowerCase()}${classes}> extends to ${Math.round(box.right)}px`;
      });
  });
}

function describeViolation(violation) {
  const targets = violation.nodes
    .slice(0, 3)
    .map((node) => node.target.join(" "))
    .join(", ");
  return `${violation.id} (${violation.impact ?? "unknown"}): ${violation.help} [${targets}]`;
}

async function main() {
  const siteDir = resolve(process.argv[2] ?? "public");
  const routes = routesFor(siteDir);

  if (routes.length === 0) {
    console.error(`no generated HTML documents found in ${siteDir}`);
    return 1;
  }

  const { server, origin, meter } = await startServer(siteDir);
  const browser = await chromium.launch({ channel: "chromium-headless-shell" });
  const failures = [];
  const weights = [];
  let checks = 0;

  try {
    for (const viewport of VIEWPORTS) {
      const context = await browser.newContext({
        viewport: { width: viewport.width, height: viewport.height },
      });
      const page = await context.newPage();

      for (const route of routes) {
        const label = `${route} @ ${viewport.name} (${viewport.width}px)`;
        const response = await page.goto(`${origin}${route}`, { waitUntil: "load" });

        if (!response?.ok()) {
          failures.push(`${label}: server returned ${response?.status() ?? "no response"}`);
          continue;
        }

        const { violations } = await new AxeBuilder({ page }).withTags(AXE_TAGS).analyze();
        for (const violation of violations) {
          failures.push(`${label}: ${describeViolation(violation)}`);
        }

        for (const problem of await fontProblems(page)) {
          failures.push(`${label}: ${problem}`);
        }

        for (const element of await overflowingElements(page)) {
          failures.push(`${label}: horizontal overflow: ${element}`);
        }
        checks += 1;
      }

      await context.close();
    }

    // Weight is measured in its own pass, one fresh context per route, so no
    // route is scored against a cache warmed by the previous one.
    for (const route of routes) {
      const context = await browser.newContext();
      const page = await context.newPage();

      meter.bytes = 0;
      await page.goto(`${origin}${route}`, { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      const bytes = meter.bytes;
      weights.push({ route, bytes });

      if (bytes > PAGE_WEIGHT_BUDGET) {
        failures.push(
          `${route}: page weight ${(bytes / 1024).toFixed(1)} KiB exceeds the ` +
            `${(PAGE_WEIGHT_BUDGET / 1024).toFixed(0)} KiB budget`,
        );
      }
      await context.close();
    }
  } finally {
    await browser.close();
    await new Promise((done) => server.close(done));
  }

  if (failures.length > 0) {
    console.error("browser quality checks failed:");
    for (const failure of failures) {
      console.error(`- ${failure}`);
    }
    return 1;
  }

  console.log(
    `checked ${routes.length} route(s) across ${VIEWPORTS.length} viewport(s) ` +
      `(${checks} page loads) in ${relative(process.cwd(), siteDir) || siteDir}`,
  );
  console.log(
    `no ${AXE_TAGS.join("/")} violations, no horizontal overflow, ` +
      `and ${WEBFONT_FAMILY} loaded in every run`,
  );
  for (const { route, bytes } of weights) {
    console.log(
      `  ${route} — ${(bytes / 1024).toFixed(1)} KiB ` +
        `of the ${(PAGE_WEIGHT_BUDGET / 1024).toFixed(0)} KiB budget`,
    );
  }
  return 0;
}

process.exit(await main());
