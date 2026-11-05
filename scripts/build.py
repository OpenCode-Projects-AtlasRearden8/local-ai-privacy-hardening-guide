#!/usr/bin/env python3
"""Build the Local AI Privacy Hardening Guide site.

Reads docs/*.md, renders each page to site/*.html plus a shared stylesheet
and index. Uses only the Python standard library plus the `markdown`
package; falls back to a minimal built-in renderer if `markdown` is not
installed. Links written as `something.md` in the docs are rewritten to
`something.html` in the generated HTML so both GitHub previews and the
static site work from the same source files.
"""

import html
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
SITE = os.path.join(ROOT, "site")
ASSETS = os.path.join(ROOT, "assets")

TITLE = "Local AI Privacy Hardening Guide"
TAGLINE = "A follow-up manual by Asdale Dynamics, LLC"

PAGES = [
    "index",
    "01-ports-and-firewall",
    "02-model-files-and-cache-hygiene",
    "03-where-chats-persist-on-disk",
    "04-autosave-and-screenshot-risks",
    "05-shell-history-hygiene",
    "06-monthly-privacy-reset-ritual",
    "hardening-checklist",
    "glossary",
]

NAV_LABELS = {
    "index": "Start here",
    "01-ports-and-firewall": "Ports &amp; firewall",
    "02-model-files-and-cache-hygiene": "Model &amp; cache hygiene",
    "03-where-chats-persist-on-disk": "Where chats live",
    "04-autosave-and-screenshot-risks": "Autosave &amp; screenshots",
    "05-shell-history-hygiene": "Shell history",
    "06-monthly-privacy-reset-ritual": "Monthly reset",
    "hardening-checklist": "Checklist",
    "glossary": "Glossary",
}

try:
    import markdown as _md

    _MD_KWARGS = {"extensions": ["extra", "sane_lists"], "output_format": "html5"}
except ImportError:
    _md = None

# ---------------------------------------------------------------------------
# Minimal fallback renderer (headings, lists, tables, fenced code, inline).
# Used only when the `markdown` package is unavailable.
# ---------------------------------------------------------------------------

def _inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<em>\1</em>", text)
    text = re.sub(r"\[x\]", '<input type="checkbox" checked disabled>', text)
    text = re.sub(r"\[ \]", '<input type="checkbox" disabled>', text)
    return text


def _fallback_render(md_text: str) -> str:
    out = []
    in_code = False
    code_lines = []
    list_stack = []
    in_para = False
    table_lines: list = []
    para = []

    def close_para():
        nonlocal in_para
        if para:
            out.append("<p>%s</p>" % _inline(" ".join(para)))
            para.clear()
            in_para = False

    def close_list():
        while list_stack:
            out.append("</%s>" % list_stack.pop())

    def close_table():
        if not table_lines:
            return
        rows = [ln for ln in table_lines if not re.match(r"^\s*\|[\s\-:|]+\|\s*$", ln)]
        out.append("<table>")
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            out.append("<tr>" + "".join("<%s>%s</%s>" % (tag, _inline(c), tag) for c in cells) + "</tr>")
        out.append("</table>")
        table_lines.clear()

    for line in md_text.splitlines():
        if line.startswith("```"):
            close_para(); close_table(); close_list()
            if not in_code:
                in_code = True
                out.append("<pre><code>")
            else:
                in_code = False
                out.append("</code></pre>")
            continue
        if in_code:
            out.append(html.escape(line, quote=False))
            continue
        if re.match(r"^\s*\|.*\|\s*$", line):
            close_para(); close_list()
            table_lines.append(line)
            continue
        close_table()
        m_heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m_heading:
            close_para(); close_list()
            level = len(m_heading.group(1))
            out.append("<h%d>%s</h%d>" % (level, _inline(m_heading.group(2).strip()), level))
            continue
        if not line.strip():
            close_para(); close_list()
            continue
        if line.strip() == "---":
            close_para(); close_list()
            out.append("<hr>")
            continue
        m_item = re.match(r"^(\s*)([-*+])\s+(.*)$", line)
        if m_item:
            close_para()
            indent = len(m_item.group(1)) // 2
            while list_stack and len(list_stack) > indent + 1:
                out.append("</%s>" % list_stack.pop())
            while len(list_stack) < indent + 1:
                out.append("<ul>")
                list_stack.append("ul")
            out.append("<li>%s</li>" % _inline(m_item.group(3)))
            continue
        m_num = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m_num:
            close_para()
            while list_stack and list_stack[-1] == "ul":
                out.append("</ul>")
                list_stack.pop()
            if not list_stack:
                out.append("<ol>")
                list_stack.append("ol")
            out.append("<li>%s</li>" % _inline(m_num.group(3)))
            continue
        if re.match(r"^>\s?", line):
            close_para(); close_list()
            out.append("<blockquote><p>%s</p></blockquote>" % _inline(re.sub(r"^>\s?", "", line)))
            continue
        para.append(line.strip())
        in_para = True
    close_para(); close_table(); close_list()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def render(text: str) -> str:
    if _md is not None:
        return _md.markdown(text, **_MD_KWARGS)
    return _fallback_render(text).replace("<pre><code>\n", "<pre><code>")


def fix_task_lists(body: str) -> str:
    body = re.sub(r"<li>\[ \]\s*", '<li><input type="checkbox"> ', body)
    body = re.sub(r"<li>\[[xX]\]\s*", '<li><input type="checkbox" checked> ', body)
    return body


def rewrite_links(body: str) -> str:
    # Local .md links become .html links in the site output.
    return re.sub(r'href="([^":#]+)\.md"', r'href="\1.html"', body)


def page_shell(slug: str, body_html: str) -> str:
    nav = []
    for p in PAGES:
        cur = ' aria-current="page"' if p == slug else ""
        nav.append('<a href="%s.html"%s>%s</a>' % (p, cur, NAV_LABELS[p]))
    return TEMPLATE.format(
        title=TITLE,
        label=NAV_LABELS[slug],
        nav="".join(nav),
        body=body_html,
        tagline=TAGLINE,
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &mdash; {label}</title>
<meta name="description" content="Plain-English guide to locking down a local AI setup: ports, firewall rules, model and cache hygiene, chat persistence, autosave risks, shell history, and a monthly reset ritual.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site">
  <div class="wrap">
    <p class="sitename"><a href="index.html"><span>Local AI</span> Privacy Hardening Guide</a></p>
    <nav class="topnav">{nav}</nav>
  </div>
</header>
<main class="wrap">
{body}
<div class="pagenav">
  <a href="index.html">&larr; Start here</a> &middot;
  <a href="hardening-checklist.html">Hardening checklist</a> &middot;
  <a href="glossary.html">Glossary</a>
</div>
</main>
<footer class="site">
  <div class="wrap">
    <p>{title} &middot; {tagline} &middot; MIT License &middot; Education only &mdash; not security, legal, or medical advice.</p>
  </div>
</footer>
</body>
</html>
"""


def main() -> int:
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    shutil.copy(os.path.join(ASSETS, "style.css"), os.path.join(SITE, "style.css"))
    for slug in PAGES:
        src = os.path.join(DOCS, slug + ".md")
        with open(src, encoding="utf-8") as fh:
            body = rewrite_links(fix_task_lists(render(fh.read())))
        with open(os.path.join(SITE, slug + ".html"), "w", encoding="utf-8") as fh:
            fh.write(page_shell(slug, body))
        print("built %s.html" % slug)
    print("site -> %s" % SITE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
