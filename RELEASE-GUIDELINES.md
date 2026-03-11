# RELEASE-GUIDELINES

This document outlines the standard process for publishing a release in the `iryna-watch` project. It reflects a commitment to editorial dignity, technical clarity, and transparent infrastructure.

---

## 🧭 When to Create a Release

Create a release when:

- A major feature (e.g. RSS feed, glossary module, timeline expansion) is finalized
- Editorial or technical hygiene reaches a milestone (e.g. validator compliance, cache tuning)
- Infrastructure changes affect public deployment (e.g. Netlify config, repo sync)
- Contributor onboarding or public syndication is ready

---

## 🏷️ Release Tag Format

Use semantic or descriptive tags:

- `v1.0-rss-ready`
- `v1.1-glossary-module`
- `v1.2-cache-tuning`
- `v2.0-timeline-expansion`

---

## 📦 Release Checklist

Before publishing a release:

- [ ] Prior to merging PRs, test the Netlify deployment preview
- [ ] Merge all relevant PRs to `main`
- [ ] Confirm Netlify deployment is live and accurate
- [ ] Validate RSS feed via W3C and browser preview
- [ ] Confirm editorial hygiene (markup, ampersands, scoped GUIDs)
- [ ] Update `_headers` for cache control if needed
- [ ] Confirm mobile-first layout and accessibility
- [ ] Update footer release tag (auto via GitHub API)

---

## 📝 How to Publish a Release

1. Go to GitHub → your repo → **Releases**
2. Click **“Draft a new release”**
3. Fill out:
   - **Tag version**: `vX.Y-description`
   - **Target branch**: `main`
   - **Title**: Short summary (e.g. `RSS feed deployed`)
   - **Description**:

     ```markdown
     - Validator-compliant RSS feed and generator script
     - Editorial hygiene: ampersand sanitization, scoped GUIDs
     - Feed discoverability via <link rel="alternate">
     - Cache-control headers for respectful freshness
     - Netlify deployment confirmed
     ```

4. Click **“Publish release”**

---

## 🔁 Post-Release Actions

- [ ] Confirm footer displays correct release tag
- [ ] Optionally tag a milestone in `RELEASE-README.md`
- [ ] Update `CONTRIBUTING.md` if onboarding changes
- [ ] Announce release (social, email, internal)

---

## 🧠 Editorial Philosophy

All releases reflect:

- Respectful handling of trauma and legal documentation
- Transparent infrastructure and contributor clarity
- Modular, auditable systems for principled participation

---
