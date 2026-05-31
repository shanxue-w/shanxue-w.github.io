# Hao Wang Personal Homepage

This repository contains a MkDocs-based personal academic homepage.

## Local Preview

```bash
mkdocs serve
```

Then open the printed local URL.

## Build

```bash
mkdocs build --strict --clean
```

The built site is written to `site/`.

## Test

```bash
python3 tests/test_site_build.py
```

The test builds the MkDocs site into `_site_test/` and checks the rendered homepage.

## Editing Content

- Main homepage content: `docs/index.md`
- CV landing page: `docs/cv.md`
- Downloadable CV PDF: `docs/files/WangHao_CV.pdf`
- Profile metadata and navigation: `mkdocs.yml`
- Layout template: `overrides/base.html`
- Site styles: `docs/assets/css/site.css`

Replace `docs/assets/img/avatar-placeholder.svg` with a personal photo when ready, and update `mkdocs.yml` if the filename changes.
