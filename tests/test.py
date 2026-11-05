#!/usr/bin/env python3
"""Tests for the Local AI Privacy Hardening Guide build.

Verifies that every docs page exists, every internal link resolves,
the generated site matches the docs (no stale files), the fallback
renderer produces the same structural elements, and the expected
headings/keywords survive conversion. Run: python3 tests/test.py
"""

import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.chdir(ROOT)

import build  # noqa: E402


class BuildTests(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        cls.result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "scripts", "build.py")],
            capture_output=True, text=True,
        )
        cls.site = build.SITE

    def test_build_script_exits_zero(self):
        self.assertEqual(self.result.returncode, 0, self.result.stderr)

    def test_every_docs_page_built(self):
        for p in build.PAGES:
            self.assertTrue(
                os.path.exists(os.path.join(build.DOCS, p + ".md")),
                "missing docs file for %s" % p,
            )
            self.assertTrue(
                os.path.exists(os.path.join(self.site, p + ".html")),
                "missing built page %s.html" % p,
            )
        self.assertTrue(os.path.exists(os.path.join(self.site, "style.css")))

    def test_no_unbuilt_stray_pages(self):
        built = [p + ".html" for p in build.PAGES] + ["style.css"]
        for entry in os.listdir(self.site):
            self.assertIn(entry, built, "stale/unknown file in site/: %s" % entry)

    def test_pages_have_expected_structure(self):
        for p in build.PAGES:
            with open(os.path.join(self.site, p + ".html"), encoding="utf-8") as fh:
                text = fh.read()
            self.assertIn("<!DOCTYPE html>", text)
            self.assertIn("</html>", text)
            self.assertIn('<link rel="stylesheet" href="style.css">', text)
            self.assertIn("<h1>", text)
            # No unconverted markdown leaking through
            self.assertNotIn("```", text)
            self.assertNotIn("##", text.split("<body>", 1)[1])

    def test_internal_links_resolve(self):
        for p in build.PAGES:
            with open(os.path.join(self.site, p + ".html"), encoding="utf-8") as fh:
                text = fh.read()
            for href in re.findall(r'href="([^"]+)\.html"', text):
                self.assertIn(
                    os.path.exists(os.path.join(self.site, href + ".html")),
                    {True},
                    "%s links to missing page %s.html" % (p, href),
                )

    def test_md_links_rewritten_in_site(self):
        with open(os.path.join(self.site, "index.html"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertNotRegex(text, r'href="[^"]+\.md"')

    def test_checklist_has_checkboxes(self):
        with open(os.path.join(self.site, "hardening-checklist.html"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn('type="checkbox"', text)

    def test_code_blocks_render_as_pre(self):
        with open(os.path.join(self.site, "01-ports-and-firewall.html"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("<pre>", text)
        self.assertIn("ufw", text)

    def test_tables_render(self):
        with open(os.path.join(self.site, "03-where-chats-persist-on-disk.html"), encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("<table>", text)
        self.assertIn("<th>", text)

    def test_fallback_renderer(self):
        original = build._md
        build._md = None
        try:
            html_out = build.render("# Hi\n\nSome **bold** text.\n\n- item one\n- item two\n\n```bash\necho hi\n```\n")
        finally:
            build._md = original
        self.assertIn("<h1>Hi</h1>", html_out)
        self.assertIn("<strong>bold</strong>", html_out)
        self.assertIn("<li>item one</li>", html_out)
        self.assertIn("<pre><code>echo hi", html_out)
    def test_no_secrets_in_repo(self):
        pattern = re.compile(
            r"sk-[A-Za-z0-9]{16,}"
            r"|AKIA[0-9A-Z]{16}"
            r"|ghp_[A-Za-z0-9]{20,}"
            r"|-----BEGIN [A-Z]+ PRIVATE KEY-----"
        )
        for dirpath, _dirs, files in os.walk(ROOT):
            if any(skip in dirpath for skip in (".git", "site", "__pycache__")):
                continue
            for name in files:
                with open(os.path.join(dirpath, name), encoding="utf-8", errors="ignore") as fh:
                    self.assertIsNone(pattern.search(fh.read()), "possible secret in %s" % name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
