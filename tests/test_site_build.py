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

    def test_mkdocs_build_renders_homepage_profile_and_publication_card(self):
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
        publications_html = (BUILD_DIR / "publications/index.html").read_text(encoding="utf-8")
        research_html = (BUILD_DIR / "research/index.html").read_text(encoding="utf-8")
        awards_html = (BUILD_DIR / "awards/index.html").read_text(encoding="utf-8")
        sitemap_xml = (BUILD_DIR / "sitemap.xml").read_text(encoding="utf-8")
        robots_path = BUILD_DIR / "robots.txt"
        index_text = html.unescape(re.sub(r"<[^>]+>", "", index_html))
        publications_text = html.unescape(re.sub(r"<[^>]+>", "", publications_html))

        title_match = re.search(r"<title>(.*?)</title>", index_html)
        self.assertIsNotNone(title_match)
        self.assertEqual("Welcome to Hao Wang's Homepage", html.unescape(title_match.group(1)))
        self.assertIn('<link rel="canonical" href="https://haowangmath.org/">', index_html)
        self.assertIn('<link rel="canonical" href="https://haowangmath.org/publications/">', publications_html)
        self.assertIn('<link rel="canonical" href="https://haowangmath.org/research/">', research_html)
        self.assertIn('<link rel="canonical" href="https://haowangmath.org/awards/">', awards_html)
        self.assertIn("<loc>https://haowangmath.org/</loc>", sitemap_xml)
        self.assertIn("<loc>https://haowangmath.org/publications/</loc>", sitemap_xml)
        self.assertIn("<loc>https://haowangmath.org/research/</loc>", sitemap_xml)
        self.assertIn("<loc>https://haowangmath.org/awards/</loc>", sitemap_xml)
        self.assertNotIn("http://haowangmath.org", sitemap_xml)
        self.assertTrue(robots_path.is_file())
        robots_txt = robots_path.read_text(encoding="utf-8")
        self.assertIn("User-agent: *", robots_txt)
        self.assertIn("Allow: /", robots_txt)
        self.assertIn("Sitemap: https://haowangmath.org/sitemap.xml", robots_txt)
        self.assertNotIn("http://haowangmath.org", robots_txt)

        self.assertIn("profile-hero", index_html)
        self.assertNotIn("profile-sidebar", index_html)
        self.assertIn("assets/img/hao-wang.jpg", index_html)
        self.assertNotIn("assets/img/avatar-placeholder.svg", index_html)
        self.assertIn('alt="Photo of Hao Wang"', index_html)
        self.assertTrue((ROOT / "docs/assets/img/hao-wang.jpg").is_file())
        self.assertIn("Hao Wang", index_html)
        self.assertIn("wanghaomathe@gmail.com", index_html)
        self.assertIn("https://github.com/shanxue-w", index_html)
        self.assertIn('href="https://scholar.google.com/citations?hl=en&user=2jZ-Kq8AAAAJ"', index_html)
        self.assertNotIn('href="https://scholar.google.com/"', index_html)
        self.assertIn("https://www.linkedin.com/in/hao-wang-0531343a5/", index_html)
        self.assertIn("https://orcid.org/0009-0005-4075-897X", index_html)
        self.assertIn("https://www.researchgate.net/profile/Hao-Wang-619", index_html)
        self.assertNotIn("https://orcid.org/my-orcid", index_html)
        self.assertIn('href="mailto:wanghaomathe@gmail.com"', index_html)
        self.assertIn('aria-label="GitHub"', index_html)
        self.assertIn('aria-label="Google Scholar"', index_html)
        self.assertIn('aria-label="LinkedIn"', index_html)
        self.assertIn('aria-label="ORCID"', index_html)
        self.assertIn('aria-label="ResearchGate"', index_html)
        self.assertNotIn('aria-label="Email"', index_html)
        self.assertIn("<span>ResearchGate</span>", index_html)
        self.assertNotIn("<span>Researchgate</span>", index_html)
        self.assertNotIn("<span>Email</span>", index_html)
        self.assertIn("assets/icons/github.svg", index_html)
        self.assertIn("assets/icons/google-scholar.svg", index_html)
        self.assertIn("assets/icons/linkedin.svg", index_html)
        self.assertIn("assets/icons/orcid.svg", index_html)
        self.assertIn("assets/icons/researchgate.svg", index_html)
        self.assertNotIn("assets/icons/email.svg", index_html)
        self.assertEqual(5, len(re.findall(r'<img class="social-icon"[^>]+ width="18" height="18"', index_html)))
        self.assertNotIn("font-awesome.min.css", index_html)
        self.assertNotIn('class="fa ', index_html)
        site_css = (BUILD_DIR / "assets/css/site.css").read_text(encoding="utf-8")
        researchgate_svg = (ROOT / "docs/assets/icons/researchgate.svg").read_text(encoding="utf-8")
        self.assertNotIn("<text", researchgate_svg)
        self.assertNotIn("<rect", researchgate_svg)
        self.assertIn("M19.586 0c", researchgate_svg)
        self.assertIn('fill="#00ccbb"', researchgate_svg)
        self.assertIn("align-items: center", site_css)
        self.assertIn("inline-size: 18px", site_css)
        self.assertIn("block-size: 18px", site_css)
        self.assertIn("min-height: 34px", site_css)
        self.assertIn(".social-icon", site_css)
        self.assertIn("object-fit: cover", site_css)
        self.assertIn("Structure-Preserving Operator Learning", index_html)
        self.assertIn("Incoming Ph.D. student", index_html)
        self.assertIn("National University of Singapore", index_html)
        self.assertIn("undergraduate student", index_html)
        news_pos = index_html.index('id="news"')
        education_pos = index_html.index('id="education"')
        self.assertLess(news_pos, education_pos)
        self.assertNotIn('id="selected-publications"', index_html)
        self.assertNotIn("Continued work on structure-preserving operator learning and scientific machine learning", index_text)
        self.assertIn("2026 One manuscript on learning missing physics from legacy simulators was accepted.", index_text)
        self.assertNotIn("2025 One manuscript on learning missing physics from legacy simulators was accepted.", index_text)
        self.assertNotIn("GPA:", index_html)
        self.assertNotIn("Relevant coursework", index_html)
        self.assertNotIn("Download PDF", index_html)
        self.assertNotIn("WangHao_CV.pdf", index_html)
        self.assertNotIn("+86 152 7099 8779", index_html)
        self.assertIn('href="publications/">Publications</a>', index_html)
        self.assertIn('href="research/">Research</a>', index_html)
        self.assertIn('href="awards/">Awards</a>', index_html)

        self.assertNotIn("publication-card", index_html)
        self.assertNotIn("Selected Publications", index_html)
        self.assertNotIn("assets/img/publication-placeholder.svg", index_html)
        self.assertNotIn("Learning missing physics from legacy simulators with alternating neural integrators", index_html)
        self.assertNotIn("Hao Wang, Qinghe Wang, Caiyou Yuan, and Kailiang Wu", index_text)
        self.assertNotIn("Accepted, 2026", index_html)
        self.assertNotIn("Abstract", index_html)
        self.assertNotIn("Citations:", index_html)
        self.assertNotIn(">Paper<", index_html)
        self.assertNotIn(">Code<", index_html)

        self.assertNotIn("publication-card", publications_html)
        self.assertNotIn("publication-placeholder.svg", publications_html)
        self.assertIn("<ol>", publications_html)
        self.assertIn('id="preprints"', publications_html)
        self.assertIn('id="journal-articles"', publications_html)
        preprints_pos = publications_html.index('id="preprints"')
        journal_articles_pos = publications_html.index('id="journal-articles"')
        self.assertLess(preprints_pos, journal_articles_pos)
        self.assertIn("LGNO: A local–global neural operator for hyperbolic conservation laws", publications_html)
        self.assertIn("Hao Wang, Chi-Wang Shu, and Qi Tang. Submitted, 2026.", publications_text)
        self.assertNotIn("JCP, submitted", publications_text)
        self.assertIn("Hao Wang and Qi Tang. Submitted, double-blind peer review, 2026.", publications_text)
        self.assertIn("Learning missing physics from legacy simulators with alternating neural integrators", publications_html)
        self.assertIn(
            "Hao Wang, Qinghe Wang, Caiyou Yuan, and Kailiang Wu. "
            "Article in press, Nature Communications, 2026.",
            publications_text,
        )
        self.assertIn("Article in press, <strong>Nature Communications</strong>, <strong>2026</strong>.", publications_html)
        self.assertNotIn("DOI:", publications_text)
        self.assertNotIn("10.1038/s41467-026-74002-2", publications_html)
        self.assertNotIn("https://doi.org/10.1038/s41467-026-74002-2", publications_html)
        self.assertNotIn("Accepted, 2026", publications_text)
        self.assertIn("Submitted, <strong>2026</strong>.", publications_html)
        self.assertIn("Submitted, double-blind peer review, <strong>2026</strong>.", publications_html)
        self.assertIn('<ol start="3">', publications_html)
        lgno_pos = publications_text.index("LGNO: A local–global neural operator for hyperbolic conservation laws")
        blinded_preprint_pos = publications_text.index("Hao Wang and Qi Tang. Submitted, double-blind peer review, 2026.")
        accepted_publication_pos = publications_text.index("Learning missing physics from legacy simulators with alternating neural integrators")
        self.assertLess(lgno_pos, blinded_preprint_pos)
        self.assertLess(blinded_preprint_pos, accepted_publication_pos)
        self.assertNotIn("H. Wang", publications_text)
        self.assertNotIn("Q. Tang", publications_text)

        self.assertIn("Research Intern, Georgia Institute of Technology", research_html)
        self.assertIn("https://tangqi.github.io/", research_html)
        self.assertIn("Supervisor: <a href=\"https://tangqi.github.io/\">Prof. Qi Tang</a>", research_html)
        self.assertIn("2025.12-2026.04", research_html)
        self.assertIn("2025.07-2025.08", research_html)
        self.assertIn("2024.03-2025.05", research_html)
        self.assertIn("2022.09-Present", index_html)
        self.assertIsNone(re.search(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b", index_html))
        self.assertNotIn("2026.4", index_html)
        self.assertNotIn("Mentor:", index_html)
        self.assertNotIn("Remote Research Collaborator", index_html)
        self.assertNotIn("Early 2025 - Present", index_html)
        self.assertNotIn("*** Add File", research_html)
        self.assertNotIn("Chu Kochen Scholarship", research_html)
        self.assertNotIn("Honors &amp; Awards", research_html)
        self.assertNotIn("Fourier Analysis Reading Group", research_html)
        self.assertIn("Chu Kochen Scholarship", awards_html)
        self.assertIn("Fourier Analysis Reading Group", awards_html)
        self.assertIn('data-goatcounter="https://haowangmath.goatcounter.com/count"', index_html)
        self.assertIn("https://gc.zgo.at/count.js", index_html)

        site_js = (BUILD_DIR / "assets/js/site.js").read_text(encoding="utf-8")
        self.assertIn("window.__pageViews", site_js)
        self.assertIn("/counter/", site_js)

    def test_cv_tex_mentions_incoming_nus_phd(self):
        cv_tex = (ROOT / "WangHao_CV.tex").read_text(encoding="utf-8")

        self.assertIn("Incoming Ph.D. Student", cv_tex)
        self.assertIn("National University of Singapore", cv_tex)

    def test_publications_markdown_is_generated_from_data(self):
        result = subprocess.run(
            ["python3", "scripts/generate_publications.py", "--check"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

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
