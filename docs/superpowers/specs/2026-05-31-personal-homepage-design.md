# Personal Homepage Design

## Goal

Build a GitHub Pages-ready personal academic homepage for Hao Wang. The site should follow the selected A-style reference direction: a single academic homepage with a fixed personal-information sidebar and anchor navigation.

## Architecture

The site will use MkDocs so that primary content is edited as Markdown. MkDocs will render `docs/index.md` and `docs/cv.md`; a small theme override will provide the academic sidebar and header layout. Styling and small interactions live in static assets under `docs/assets/`.

## Content Scope

Initial content is adapted conservatively from `WangHao_CV.pdf`, because the CV is known to be stale. The page includes About, News, Publications and Manuscripts, Education, Research Experience, Research Projects, Honors and Awards, Reading Groups, Leadership, and Technical Skills.

The public webpage must not expose the phone number from the old CV. The existing PDF remains available as a downloadable file.

## Files

- `mkdocs.yml`: MkDocs configuration, navigation, metadata, and profile fields.
- `docs/index.md`: Main homepage content in Markdown.
- `docs/cv.md`: Short CV page that links to the PDF and points users back to the homepage sections.
- `docs/files/WangHao_CV.pdf`: Copy of the current CV PDF for download.
- `overrides/base.html`: Custom MkDocs template implementing the A-style sidebar layout.
- `docs/assets/css/site.css`: Visual design and responsive layout.
- `docs/assets/js/site.js`: Small progressive enhancement for active nav state and mobile nav toggling.
- `docs/assets/img/avatar-placeholder.svg`: Replaceable profile placeholder image.
- `tests/test_site_build.py`: Acceptance test that builds the site and checks key rendered content.

## Verification

Run `python3 tests/test_site_build.py` to build through MkDocs and inspect the rendered homepage. Run `mkdocs build --strict --clean` as a direct build check. Start `mkdocs serve` for local preview.
