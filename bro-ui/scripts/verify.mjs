#!/usr/bin/env node
// bro-ui verify pass, automated part (rules 28, 30, 31, 32).
//
//   npm i -D playwright && npx playwright install chromium
//   node verify.mjs http://localhost:3000 [--out ./bro-ui-shots] [--tabs 40]
//
// For each width (320, 768, 1440) and theme (light, dark) it loads the page and reports:
//   - console errors and warnings, uncaught exceptions, failed requests  (rule 28)
//   - horizontal page overflow and the widest offending elements        (rule 30)
//   - text whose contrast is under 4.5:1 (3:1 for large text)           (rule 31)
//   - interactive elements smaller than 24x24px                          (rule 13)
//   - a Tab walk: elements that take focus with no visible focus style   (rule 32)
// and saves a full-page screenshot of each run. Exit code 1 when anything fails.
// It cannot click through flows or judge looks: rules 29 and 33 stay manual.

import { chromium } from "playwright";
import { mkdirSync } from "node:fs";

const args = process.argv.slice(2);
const url = args.find((a) => !a.startsWith("--"));
const opt = (name, dflt) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : dflt;
};
if (!url) {
  console.error("usage: node verify.mjs URL [--out DIR] [--tabs N]");
  process.exit(2);
}
const outDir = opt("out", "./bro-ui-shots");
const tabs = Number(opt("tabs", 40));
mkdirSync(outDir, { recursive: true });

const WIDTHS = [320, 768, 1440];
const THEMES = ["light", "dark"];

// Runs inside the page. Kept self-contained (no closures over Node scope).
function audit() {
  const parse = (c) => {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0] / 255, g: p[1] / 255, b: p[2] / 255, a: p.length > 3 ? p[3] : 1 };
  };
  const lin = (c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
  const lum = (c) => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const ratio = (a, b) => {
    const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p);
    return (x + 0.05) / (y + 0.05);
  };
  const blend = (top, under) => ({
    r: top.r * top.a + under.r * (1 - top.a),
    g: top.g * top.a + under.g * (1 - top.a),
    b: top.b * top.a + under.b * (1 - top.a),
    a: 1,
  });
  // Effective background: walk up and composite translucent layers. Images and gradients are skipped.
  const bgOf = (el) => {
    const layers = [];
    for (let n = el; n; n = n.parentElement) {
      const c = parse(getComputedStyle(n).backgroundColor);
      if (c && c.a > 0) {
        layers.push(c);
        if (c.a >= 1) break;
      }
    }
    let acc = { r: 1, g: 1, b: 1, a: 1 };
    for (let i = layers.length - 1; i >= 0; i--) acc = blend(layers[i], acc);
    return acc;
  };
  const label = (el) =>
    el.tagName.toLowerCase() +
    (el.id ? "#" + el.id : "") +
    (typeof el.className === "string" && el.className.trim()
      ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".")
      : "");
  const visible = (el) => {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none" && Number(s.opacity) > 0;
  };

  const doc = document.documentElement;
  const overflow = doc.scrollWidth - doc.clientWidth;
  const wide = [];
  if (overflow > 0) {
    for (const el of document.body.querySelectorAll("*")) {
      const r = el.getBoundingClientRect();
      if (r.right > doc.clientWidth + 1 && visible(el)) wide.push(`${label(el)} right=${Math.round(r.right)}`);
      if (wide.length >= 5) break;
    }
  }

  const lowContrast = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode;
    const el = t.parentElement;
    if (!el || seen.has(el) || !t.textContent.trim() || !visible(el)) continue;
    seen.add(el);
    const s = getComputedStyle(el);
    const fg = parse(s.color);
    if (!fg) continue;
    const bg = bgOf(el);
    const r = ratio(blend(fg, bg), bg);
    const size = parseFloat(s.fontSize);
    const bold = Number(s.fontWeight) >= 700;
    const large = size >= 24 || (bold && size >= 18.66);
    const need = large ? 3 : 4.5;
    if (r < need) lowContrast.push(`${label(el)} "${t.textContent.trim().slice(0, 30)}" ${r.toFixed(2)}:1 < ${need}:1`);
  }

  const small = [];
  const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [role=link], [role=checkbox], [role=tab], [role=menuitem]';
  for (const el of document.querySelectorAll(sel)) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    // WCAG 2.5.8 exempts links inside running text
    const inline = el.tagName === "A" && getComputedStyle(el).display === "inline" && el.parentElement?.closest("p, li");
    if (!inline && (r.width < 24 || r.height < 24)) small.push(`${label(el)} ${Math.round(r.width)}x${Math.round(r.height)}`);
  }

  return { overflow, wide, lowContrast: lowContrast.slice(0, 15), lowCount: lowContrast.length, small: small.slice(0, 15), smallCount: small.length };
}

function focusStyle() {
  const el = document.activeElement;
  if (!el || el === document.body) return null;
  const s = getComputedStyle(el);
  const shown =
    (s.outlineStyle !== "none" && parseFloat(s.outlineWidth) > 0) ||
    (s.boxShadow && s.boxShadow !== "none");
  const name = el.tagName.toLowerCase() + (el.id ? "#" + el.id : "");
  return { name, shown };
}

let failed = false;
const browser = await chromium.launch();
for (const theme of THEMES) {
  for (const width of WIDTHS) {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, colorScheme: theme });
    const page = await ctx.newPage();
    const logs = [];
    page.on("console", (m) => {
      if (m.type() === "error" || m.type() === "warning") logs.push(`console.${m.type()}: ${m.text().slice(0, 160)}`);
    });
    page.on("pageerror", (e) => logs.push(`uncaught: ${String(e).slice(0, 160)}`));
    page.on("requestfailed", (r) => logs.push(`request failed: ${r.url().slice(0, 120)} ${r.failure()?.errorText ?? ""}`));

    await page.goto(url, { waitUntil: "networkidle" });
    const a = await page.evaluate(audit);

    const noRing = new Set();
    for (let i = 0; i < tabs; i++) {
      await page.keyboard.press("Tab");
      const f = await page.evaluate(focusStyle);
      if (f && !f.shown) noRing.add(f.name);
    }

    const shot = `${outDir}/${theme}-${width}.png`;
    await page.screenshot({ path: shot, fullPage: true });

    const problems = [
      ...logs,
      ...(a.overflow > 0 ? [`horizontal overflow ${a.overflow}px: ${a.wide.join(", ")}`] : []),
      ...a.lowContrast.map((x) => `contrast: ${x}`),
      ...(a.lowCount > a.lowContrast.length ? [`contrast: ${a.lowCount - a.lowContrast.length} more`] : []),
      ...a.small.map((x) => `target under 24px: ${x}`),
      ...(a.smallCount > a.small.length ? [`target under 24px: ${a.smallCount - a.small.length} more`] : []),
      ...[...noRing].map((x) => `no visible focus: ${x}`),
    ];
    const ok = problems.length === 0;
    failed ||= !ok;
    console.log(`${ok ? "PASS" : "FAIL"}  ${theme.padEnd(5)} ${String(width).padStart(4)}px  ${shot}`);
    for (const p of problems) console.log(`      ${p}`);
    await ctx.close();
  }
}
await browser.close();
console.log(failed ? "\nverify: FAIL" : "\nverify: PASS (now do rules 29, 33 and 34 by hand)");
process.exit(failed ? 1 : 0);
