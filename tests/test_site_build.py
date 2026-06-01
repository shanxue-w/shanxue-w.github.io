import shutil
import subprocess
import unittest
import re
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "_site_test"


class MkDocsSiteBuildTest(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree(BUILD_DIR, ignore_errors=True)

    def test_mkdocs_build_renders_homepage_profile_and_cv_link(self):
        result = subprocess.run(
            [
                "mkdocs",
                "build",
                "--strict",
                "--clean",
                "--site-dir",
                str(BUILD_DIR),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

        index_html = (BUILD_DIR / "index.html").read_text(encoding="utf-8")
        title_match = re.search(r"<title>(.*?)</title>", index_html)
        self.assertIsNotNone(title_match)
        self.assertEqual("Welcome to Hao Wang's Homepage", html.unescape(title_match.group(1)))
        self.assertIn('<link rel="canonical" href="https://haowangmath.org/">', index_html)

        self.assertIn("profile-sidebar", index_html)
        self.assertIn("Hao Wang", index_html)
        self.assertIn("Structure-Preserving Operator Learning", index_html)
        self.assertIn("Incoming Ph.D. student", index_html)
        self.assertIn("National University of Singapore", index_html)
        self.assertIn("undergraduate student", index_html)
        self.assertNotIn("GPA:", index_html)
        self.assertNotIn("Relevant coursework", index_html)
        self.assertIn("WangHao_CV.pdf", index_html)
        self.assertNotIn("+86 152 7099 8779", index_html)
        self.assertIn("Research Intern, Georgia Institute of Technology", index_html)
        self.assertIn("https://tangqi.github.io/", index_html)
        self.assertIn("Supervisor: <a href=\"https://tangqi.github.io/\">Prof. Qi Tang</a>", index_html)
        self.assertIn("2025.12-2026.04", index_html)
        self.assertIn("2025.07-2025.08", index_html)
        self.assertIn("2024.03-2025.05", index_html)
        self.assertIn("2022.09-Present", index_html)
        self.assertIsNone(re.search(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b", index_html))
        self.assertNotIn("2026.4", index_html)
        self.assertNotIn("Mentor:", index_html)
        self.assertNotIn("Remote Research Collaborator", index_html)
        self.assertNotIn("Early 2025 - Present", index_html)
        self.assertIn('data-goatcounter="https://haowangmath.goatcounter.com/count"', index_html)
        self.assertIn("https://gc.zgo.at/count.js", index_html)

        site_js = (BUILD_DIR / "assets/js/site.js").read_text(encoding="utf-8")
        self.assertIn("window.__pageViews", site_js)
        self.assertIn("/counter/", site_js)

    def test_cv_tex_mentions_incoming_nus_phd(self):
        cv_tex = (ROOT / "WangHao_CV.tex").read_text(encoding="utf-8")

        self.assertIn("Incoming Ph.D. Student", cv_tex)
        self.assertIn("National University of Singapore", cv_tex)

    def test_cv_tex_is_synced_with_homepage_research_updates(self):
        cv_tex = (ROOT / "WangHao_CV.tex").read_text(encoding="utf-8")

        self.assertIn("Learning missing physics from legacy simulators with alternating neural integrators", cv_tex)
        self.assertIn("Qinghe Wang, Caiyou Yuan, Kailiang Wu", cv_tex)
        self.assertIn("Manuscript accepted", cv_tex)
        self.assertIn("Research Intern", cv_tex)
        self.assertIn("Georgia Institute of Technology", cv_tex)
        self.assertIn("2025.12-2026.04", cv_tex)
        self.assertIn("2025.07-2025.08", cv_tex)
        self.assertIn("2024.03-2025.05", cv_tex)
        self.assertIn("2022.09-Present", cv_tex)
        self.assertIsNone(re.search(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b", cv_tex))
        self.assertNotIn("2026.4", cv_tex)
        self.assertIn("Supervisor: Prof. Qi Tang", cv_tex)
        self.assertNotIn("Mentor", cv_tex)
        self.assertNotIn("hrefWithoutArrow", cv_tex)
        self.assertNotIn("https://tangqi.github.io/", cv_tex)
        self.assertNotIn("https://sites.google.com/site/klwuhomepage/", cv_tex)
        self.assertNotIn("https://person.zju.edu.cn/wangheyu", cv_tex)
        self.assertNotIn("Remote Research Collaborator", cv_tex)
        self.assertNotIn("Early 2025", cv_tex)


if __name__ == "__main__":
    unittest.main()
