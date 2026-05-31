import shutil
import subprocess
import unittest
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

        self.assertIn("profile-sidebar", index_html)
        self.assertIn("Hao Wang", index_html)
        self.assertIn("Structure-Preserving Operator Learning", index_html)
        self.assertIn("Incoming Ph.D. student", index_html)
        self.assertIn("National University of Singapore", index_html)
        self.assertIn("WangHao_CV.pdf", index_html)
        self.assertNotIn("+86 152 7099 8779", index_html)

    def test_cv_tex_mentions_incoming_nus_phd(self):
        cv_tex = (ROOT / "WangHao_CV.tex").read_text(encoding="utf-8")

        self.assertIn("Incoming Ph.D. Student", cv_tex)
        self.assertIn("National University of Singapore", cv_tex)


if __name__ == "__main__":
    unittest.main()
