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

## Updating Publications

Edit `data/publications.json`, keeping entries in the display order you want. Then regenerate the Markdown page:

```bash
python3 scripts/generate_publications.py
```

The script numbers entries continuously across sections, so the first item is `1`, the next is `2`, and later sections continue from there.

## Editing Content

- Main homepage content: `docs/index.md`
- Publications data source: `data/publications.json`
- Generated publications page: `docs/publications.md`
- Research page: `docs/research.md`
- Awards page: `docs/awards.md`
- Profile metadata and navigation: `mkdocs.yml`
- Layout template: `overrides/base.html`
- Site styles: `docs/assets/css/site.css`
- Publication placeholder image: `docs/assets/img/publication-placeholder.svg`

Replace `docs/assets/img/avatar-placeholder.svg` with a personal photo when ready, and update `mkdocs.yml` if the filename changes.
