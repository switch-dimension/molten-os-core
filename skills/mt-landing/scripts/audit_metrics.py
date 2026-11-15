#!/usr/bin/env python3
"""Deterministic landing-page audit metrics.

Computes the objective, measurable parts of the 22-point audit so the model
can interpret facts instead of eyeballing a screenshot. Standard library only
(no pip install) so it runs in any environment that has Python 3.

Usage:
    python3 audit_metrics.py path/to/index.html [extra.css ...] [--cta "Button text"]
    python3 audit_metrics.py https://example.com [--cta "Start free trial"]

Output: a JSON report on stdout. Every metric maps to a numbered audit check;
see the "check" field on each block. This script measures; it does not judge.
The verdicts (Pass/Weak/Fail) are still the reviewer's job.
"""

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------------
# Input loading
# ---------------------------------------------------------------------------


def is_url(s):
    return s.startswith("http://") or s.startswith("https://")


def fetch_url(url):
    req = Request(url, headers={"User-Agent": "landing-audit/1.0"})
    with urlopen(req, timeout=20) as resp:  # noqa: S310 - user-supplied URL is intentional
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

CLICKABLE_TAGS = {"a", "button"}
CLICKABLE_INPUT_TYPES = {"submit", "button", "image", "reset"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.clickables = []          # list of dicts: {tag, text, attrs}
        self.headings = []            # list of dicts: {level, text}
        self.images = []              # list of dicts: {src, alt, has_alt}
        self.inline_styles = []       # contents of <style> blocks
        self.linked_css = []          # hrefs of <link rel=stylesheet>
        self.font_links = []          # google fonts / preconnect hints
        self.form_controls = []       # {tag, type, id, has_label_attr, name}
        self.labels_for = set()       # 'for' targets of <label>
        self.label_wraps = 0          # labels that wrap a control (approx)
        self._capture = None          # (kind, buffer) while inside a tracked tag
        self._style_buf = []
        self._in_style = False

    # -- tag handling -------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "button"):
            self._start_capture(tag, a)
        elif tag == "input":
            itype = (a.get("type") or "text").lower()
            if itype in CLICKABLE_INPUT_TYPES:
                self.clickables.append(
                    {"tag": "input", "type": itype, "text": a.get("value", ""), "attrs": a}
                )
            else:
                self.form_controls.append(
                    {"tag": "input", "type": itype, "id": a.get("id"), "name": a.get("name")}
                )
        elif tag in ("select", "textarea"):
            self.form_controls.append(
                {"tag": tag, "type": tag, "id": a.get("id"), "name": a.get("name")}
            )
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._start_capture(tag, a)
        elif tag == "img":
            self.images.append(
                {"src": a.get("src", ""), "alt": a.get("alt"), "has_alt": "alt" in a}
            )
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            href = a.get("href", "")
            if "stylesheet" in rel:
                if "fonts.googleapis" in href or "fonts.gstatic" in href:
                    self.font_links.append(href)
                else:
                    self.linked_css.append(href)
            elif "preconnect" in rel and "fonts.g" in href:
                self.font_links.append(href)
        elif tag == "label":
            if "for" in a:
                self.labels_for.add(a["for"])
            else:
                self.label_wraps += 1
        elif tag == "style":
            self._in_style = True
            self._style_buf = []

        # Anything with onclick or role=button is clickable too.
        if tag not in ("a", "button", "input") and (
            "onclick" in a or (a.get("role", "").lower() == "button")
        ):
            self.clickables.append({"tag": tag, "text": "", "attrs": a})

    def handle_startendtag(self, tag, attrs):
        # Self-closing forms of tracked void-ish tags.
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if self._capture and self._capture[0] == tag:
            kind, buf, attrs = self._capture
            text = re.sub(r"\s+", " ", "".join(buf)).strip()
            if kind in ("a", "button"):
                self.clickables.append({"tag": kind, "text": text, "attrs": attrs})
            else:  # heading
                self.headings.append({"level": int(kind[1]), "text": text})
            self._capture = None
        if tag == "style":
            self._in_style = False
            self.inline_styles.append("".join(self._style_buf))
            self._style_buf = []

    def handle_data(self, data):
        if self._capture:
            self._capture[1].append(data)
        if self._in_style:
            self._style_buf.append(data)

    def _start_capture(self, tag, attrs):
        # If we were already capturing (nested), flush nothing; just track the
        # outer element by keeping the existing capture.
        if self._capture is None:
            self._capture = (tag, [], attrs)


# ---------------------------------------------------------------------------
# Color + contrast (WCAG 2.x)
# ---------------------------------------------------------------------------

NAMED_COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),
    "silver": (192, 192, 192),
    "transparent": None,
}


def parse_color(value):
    """Return (r, g, b) 0-255 or None if unparseable/transparent."""
    if value is None:
        return None
    v = value.strip().lower()
    if v in NAMED_COLORS:
        return NAMED_COLORS[v]
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            r, g, b = (int(c * 2, 16) for c in h[:3])
            return (r, g, b)
        if len(h) in (6, 8):
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
        return None
    m = re.fullmatch(r"rgba?\(([^)]+)\)", v)
    if m:
        parts = re.split(r"[,\s/]+", m.group(1).strip())
        nums = []
        for p in parts[:3]:
            if p.endswith("%"):
                nums.append(round(float(p[:-1]) * 255 / 100))
            else:
                try:
                    nums.append(int(round(float(p))))
                except ValueError:
                    return None
        if len(nums) == 3:
            return tuple(max(0, min(255, n)) for n in nums)
    return None


def relative_luminance(rgb):
    def chan(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def contrast_ratio(fg, bg):
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return round((hi + 0.05) / (lo + 0.05), 2)


# ---------------------------------------------------------------------------
# CSS analysis
# ---------------------------------------------------------------------------

CSS_COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)
RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}", re.DOTALL)
DECL_RE = re.compile(r"([\w-]+)\s*:\s*([^;]+)")
PX_RE = re.compile(r"(-?\d+(?:\.\d+)?)px")
VAR_DECL_RE = re.compile(r"(--[\w-]+)\s*:\s*([^;]+)")
VAR_USE_RE = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^)]+))?\)")


def strip_comments(css):
    return CSS_COMMENT.sub("", css)


def build_var_map(css):
    return {m.group(1): m.group(2).strip() for m in VAR_DECL_RE.finditer(css)}


def resolve_value(value, varmap, depth=0):
    if depth > 10:
        return value
    def repl(m):
        name, fallback = m.group(1), m.group(2)
        if name in varmap:
            return resolve_value(varmap[name], varmap, depth + 1)
        return (fallback or "").strip()
    return VAR_USE_RE.sub(repl, value).strip()


def analyze_css(css_text):
    css = strip_comments(css_text)
    varmap = build_var_map(css)

    contrast_pairs = []   # same-rule color + background pairs (high signal)
    font_sizes = []       # {selector, px}
    spacing_values = set()
    spacing_decls = []    # {selector, prop, raw}
    font_families = set()

    for rule in RULE_RE.finditer(css):
        selector = re.sub(r"\s+", " ", rule.group(1)).strip()
        body = rule.group(2)
        decls = {}
        for d in DECL_RE.finditer(body):
            decls[d.group(1).strip().lower()] = d.group(2).strip()

        # Contrast: only when a rule sets both fg and bg -> reliable pairing.
        fg_raw = decls.get("color")
        bg_raw = decls.get("background-color") or decls.get("background")
        if fg_raw and bg_raw:
            fg = parse_color(resolve_value(fg_raw, varmap))
            # background shorthand may contain more than a color; grab first token
            bg_token = resolve_value(bg_raw, varmap).split()[0] if bg_raw else None
            bg = parse_color(bg_token) if bg_token else None
            if fg and bg:
                contrast_pairs.append(
                    {
                        "selector": selector,
                        "fg": rgb_hex(fg),
                        "bg": rgb_hex(bg),
                        "ratio": contrast_ratio(fg, bg),
                    }
                )

        if "font-size" in decls:
            for px in PX_RE.findall(resolve_value(decls["font-size"], varmap)):
                font_sizes.append({"selector": selector, "px": float(px)})

        if "font-family" in decls:
            fam = resolve_value(decls["font-family"], varmap).split(",")[0].strip().strip("'\"")
            if fam:
                font_families.add(fam.lower())

        for prop in ("padding", "margin", "gap", "row-gap", "column-gap",
                     "padding-top", "padding-bottom", "padding-left", "padding-right",
                     "margin-top", "margin-bottom", "margin-left", "margin-right"):
            if prop in decls:
                raw = decls[prop]
                pxs = PX_RE.findall(raw)
                if pxs:
                    spacing_decls.append({"selector": selector, "prop": prop, "raw": raw.strip()})
                    for px in pxs:
                        spacing_values.add(float(px))

    return {
        "varmap": varmap,
        "contrast_pairs": contrast_pairs,
        "font_sizes": font_sizes,
        "spacing_values": sorted(spacing_values),
        "spacing_decls": spacing_decls,
        "font_families": sorted(font_families),
    }


def rgb_hex(rgb):
    return "#%02x%02x%02x" % rgb


# ---------------------------------------------------------------------------
# Metric assembly
# ---------------------------------------------------------------------------


def norm_text(s):
    return re.sub(r"\s+", " ", (s or "").strip()).lower()


def assemble_report(html, css_blocks, cta_text):
    parser = PageParser()
    parser.feed(html)

    all_css = "\n".join(css_blocks + parser.inline_styles)
    css = analyze_css(all_css)

    # --- Check 2: attention ratio ---
    clickable_texts = []
    for c in parser.clickables:
        t = norm_text(c.get("text", ""))
        clickable_texts.append(t)
    # Candidate CTA = most repeated non-empty clickable label.
    freq = {}
    for t in clickable_texts:
        if t:
            freq[t] = freq.get(t, 0) + 1
    candidate_cta, candidate_count = (None, 0)
    if freq:
        candidate_cta, candidate_count = max(freq.items(), key=lambda kv: kv[1])

    if cta_text:
        cta_norm = norm_text(cta_text)
        cta_count = sum(1 for t in clickable_texts if t == cta_norm)
        cta_label = cta_text
    else:
        cta_count = candidate_count
        cta_label = candidate_cta

    clickable_total = len(parser.clickables)
    ratio = round(clickable_total / cta_count, 2) if cta_count else None

    attention = {
        "check": "2 - single goal / attention ratio",
        "clickable_elements": clickable_total,
        "cta_label": cta_label,
        "cta_occurrences": cta_count,
        "ratio": ratio,
        "guide": "best landing pages run near 1:1; above 5:1 is a fail",
        "clickable_breakdown": tally([c["tag"] for c in parser.clickables]),
        "repeated_clickable_labels": sorted(
            ({"label": k, "count": v} for k, v in freq.items() if v > 1),
            key=lambda x: -x["count"],
        ),
    }

    # --- Check 4 / structure: headings ---
    h1s = [h["text"] for h in parser.headings if h["level"] == 1]
    headings = {
        "check": "4 - outcome first / single H1",
        "h1_count": len(h1s),
        "h1_text": h1s,
        "heading_outline": [{"h": h["level"], "text": h["text"]} for h in parser.headings],
        "note": "exactly one H1 expected" if len(h1s) != 1 else "single H1 ok",
    }

    # --- Check 15 / 19: contrast ---
    fails = [p for p in css["contrast_pairs"] if p["ratio"] < 4.5]
    contrast = {
        "check": "15/19 - accent + WCAG contrast",
        "pairs_measured": len(css["contrast_pairs"]),
        "pairs": sorted(css["contrast_pairs"], key=lambda p: p["ratio"]),
        "failing_AA_normal_text": fails,
        "guide": "body text needs >=4.5:1; large text / UI >=3:1. Only same-rule fg+bg pairs are measured here.",
    }

    # --- Check 18: body font size + small text ---
    sizes = css["font_sizes"]
    body_candidates = [s["px"] for s in sizes if s["selector"] in ("body", "html", ":root", "p")]
    small_text = [s for s in sizes if s["px"] < 16]
    typography = {
        "check": "18 - readable type",
        "body_font_px_candidates": sorted(set(body_candidates)),
        "declarations_under_16px": sorted(small_text, key=lambda s: s["px"]),
        "guide": "body should be >=16px so mobile doesn't zoom",
    }

    # --- Check 17: spacing rhythm ---
    one_offs = [v for v in css["spacing_values"] if v % 4 != 0]
    spacing = {
        "check": "17 - spacing rhythm",
        "distinct_px_values": css["spacing_values"],
        "off_scale_values": one_offs,
        "guide": "values should sit on a consistent step (multiples of 4 is a common scale); off-scale values look accidental. clamp()/rem-based scales won't show here.",
    }

    # --- Check 20: fonts + images ---
    typefaces = {
        "check": "7/20 - typeface count",
        "font_families": css["font_families"],
        "google_fonts_links": parser.font_links,
        "guide": "1-2 families max keeps LCP fast",
    }

    images = []
    for img in parser.images:
        entry = {"src": img["src"], "has_alt": img["has_alt"], "alt": img["alt"]}
        size = local_image_size(img["src"])
        if size is not None:
            entry["bytes"] = size
            entry["kb"] = round(size / 1024, 1)
            entry["heavy"] = size > 500 * 1024
        images.append(entry)
    image_block = {
        "check": "19/20 - images: alt text + weight",
        "count": len(images),
        "missing_alt": [i["src"] for i in images if not i["has_alt"]],
        "heavy_over_500kb": [i for i in images if i.get("heavy")],
        "images": images,
    }

    # --- Check 19: form labels ---
    unlabeled = []
    for ctrl in parser.form_controls:
        cid = ctrl.get("id")
        labeled = bool(cid and cid in parser.labels_for)
        if not labeled:
            unlabeled.append(ctrl)
    forms = {
        "check": "10/19 - form friction + labels",
        "control_count": len(parser.form_controls),
        "controls": parser.form_controls,
        "labels_for_targets": sorted(parser.labels_for),
        "wrapping_labels_approx": parser.label_wraps,
        "controls_without_for_label": unlabeled,
        "guide": "every field needs a real <label> (for= or wrapping); placeholder is not a label. Fewer fields = less friction.",
    }

    return {
        "_about": "Deterministic measurements only. Verdicts (Pass/Weak/Fail) are the reviewer's call. Some checks (rendered tap targets, real LCP) require a browser and are not covered here.",
        "attention_ratio": attention,
        "headings": headings,
        "contrast": contrast,
        "typography": typography,
        "spacing": spacing,
        "typefaces": typefaces,
        "images": image_block,
        "forms": forms,
    }


def tally(items):
    out = {}
    for i in items:
        out[i] = out.get(i, 0) + 1
    return out


_image_base_dir = None


def local_image_size(src):
    if not src or is_url(src) or src.startswith("data:"):
        return None
    if _image_base_dir is None:
        return None
    path = os.path.normpath(os.path.join(_image_base_dir, src.lstrip("/")))
    try:
        return os.path.getsize(path)
    except OSError:
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description="Deterministic landing-page audit metrics.")
    ap.add_argument("inputs", nargs="+", help="An HTML file or URL, optionally followed by CSS files.")
    ap.add_argument("--cta", help="Exact primary CTA button/link text to count precisely.")
    ap.add_argument("--compact", action="store_true", help="Compact JSON (no indentation).")
    args = ap.parse_args(argv)

    global _image_base_dir

    html = None
    css_blocks = []
    html_source = None

    for item in args.inputs:
        if is_url(item):
            content = fetch_url(item)
            if html is None:
                html = content
                html_source = item
            else:
                css_blocks.append(content)
            continue
        if not os.path.exists(item):
            sys.stderr.write(f"warning: skipping missing path {item}\n")
            continue
        text = read_file(item)
        lower = item.lower()
        if lower.endswith(".css"):
            css_blocks.append(text)
        elif html is None:
            html = text
            html_source = item
            _image_base_dir = os.path.dirname(os.path.abspath(item))
        else:
            css_blocks.append(text)

    if html is None:
        sys.stderr.write("error: no HTML input found (first arg must be an .html file or URL)\n")
        return 2

    # Auto-discover local linked CSS from the HTML if we have a base dir.
    if _image_base_dir is not None:
        probe = PageParser()
        probe.feed(html)
        for href in probe.linked_css:
            if is_url(href) or href.startswith("//"):
                continue
            path = os.path.normpath(os.path.join(_image_base_dir, href.lstrip("/")))
            if os.path.exists(path):
                css_blocks.append(read_file(path))

    report = assemble_report(html, css_blocks, args.cta)
    report["_source"] = html_source
    indent = None if args.compact else 2
    print(json.dumps(report, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
