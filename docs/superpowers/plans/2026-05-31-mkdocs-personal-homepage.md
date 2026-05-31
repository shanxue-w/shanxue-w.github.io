# MkDocs Personal Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a MkDocs-authored, A-style single-page academic homepage for Hao Wang.

**Architecture:** MkDocs renders Markdown content from `docs/index.md` and `docs/cv.md`. A custom `overrides/base.html` template provides the profile sidebar and top navigation, while CSS and JS under `docs/assets/` handle presentation and small interactions.

**Tech Stack:** MkDocs 1.1.2, Python standard-library unittest, Markdown, Jinja template override, CSS, vanilla JavaScript.

---

### Task 1: Acceptance Test

**Files:**
- Create: `tests/test_site_build.py`

- [x] **Step 1: Write the failing test**

Create a unittest that runs:

```bash
mkdocs build --strict --clean --site-dir _site_test
```

The test must assert that generated `index.html` contains `profile-sidebar`, `Hao Wang`, `Structure-Preserving Operator Learning`, and `WangHao_CV.pdf`, and does not contain the phone number from the old CV.

- [x] **Step 2: Run test to verify it fails**

Run:

```bash
python3 tests/test_site_build.py
```

Expected before implementation: failure because `mkdocs.yml` is missing.

### Task 2: MkDocs Project Files

**Files:**
- Create: `mkdocs.yml`
- Create: `docs/index.md`
- Create: `docs/cv.md`
- Create: `docs/files/WangHao_CV.pdf`
- Create: `docs/assets/img/avatar-placeholder.svg`

- [ ] **Step 1: Add MkDocs configuration**

Create `mkdocs.yml` with site metadata, `docs_dir: docs`, `site_dir: site`, built-in `mkdocs` theme plus `custom_dir: overrides`, and anchor-style navigation links in `extra.profile`.

- [ ] **Step 2: Add Markdown homepage**

Create `docs/index.md` with CV-derived sections: About, News, Publications and Manuscripts, Education, Research Experience, Research Projects, Honors and Awards, Reading Groups, Leadership, and Technical Skills.

- [ ] **Step 3: Add CV page and PDF**

Create `docs/cv.md` as a concise Markdown page linking to `files/WangHao_CV.pdf`. Copy the current `WangHao_CV.pdf` into `docs/files/WangHao_CV.pdf`.

- [ ] **Step 4: Add replaceable avatar placeholder**

Create `docs/assets/img/avatar-placeholder.svg`, a neutral profile placeholder used by the sidebar until the user provides a photo.

### Task 3: Theme Override and Assets

**Files:**
- Create: `overrides/base.html`
- Create: `docs/assets/css/site.css`
- Create: `docs/assets/js/site.js`

- [ ] **Step 1: Create theme template**

Create `overrides/base.html` with a fixed top nav, sidebar profile block, `{{ page.content }}` main content area, and footer.

- [ ] **Step 2: Add responsive CSS**

Create `docs/assets/css/site.css` with two-column desktop layout, one-column mobile layout, academic typography, compact publication and timeline sections, and no card-in-card structures.

- [ ] **Step 3: Add small JavaScript enhancement**

Create `docs/assets/js/site.js` to toggle the mobile menu and highlight active section links while scrolling.

### Task 4: Repository Setup

**Files:**
- Create: `.gitignore`
- Create: `README.md`
- Modify: `.git/` state if needed

- [ ] **Step 1: Add project docs**

Create `README.md` with local build, serve, and GitHub Pages deployment notes. Create `.gitignore` for `site/`, `_site_test/`, caches, and `.superpowers/`.

- [ ] **Step 2: Initialize Git repository**

If `.git` is still an invalid empty directory, make it writable and run `git init`.

### Task 5: Verification

**Files:**
- No new files.

- [ ] **Step 1: Run acceptance test**

Run:

```bash
python3 tests/test_site_build.py
```

Expected: `OK`.

- [ ] **Step 2: Run direct MkDocs build**

Run:

```bash
mkdocs build --strict --clean
```

Expected: build exits with code 0.

- [ ] **Step 3: Start preview server**

Run:

```bash
mkdocs serve --dev-addr 0.0.0.0:8000
```

Expected: local preview URL is available for browser inspection.
