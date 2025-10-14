# RELEASE-TAGS.md

This document outlines the tagging conventions used for GitHub releases in the `iryna-watch` project. Tags reflect editorial clarity, technical hygiene, and transparent infrastructure milestones.

---

## 🧠 Tag Philosophy

Tags should be:
- **Descriptive**: Reflect what changed (e.g. `rss-ready`, `glossary-module`)
- **Scoped**: Avoid vague labels like `update` or `fix`
- **Readable**: Use hyphens for clarity, avoid camelCase
- **Versioned**: Use semantic or milestone-style versioning

---

## 🐞 Bug Fixes

Use patch-style tags with clear scope:
- `v1.0.1-validator-fix` → XML or ampersand correction
- `v1.0.2-timeline-sort-bug` → fix for entry ordering
- `v1.0.3-feed-link-typo` → markup or metadata fix

---

## ✨ New Features

Use minor version bumps or descriptive suffixes:
- `v1.1-glossary-module` → added glossary or legal term support
- `v1.2-footer-release-tag` → auto-updating release badge
- `v1.3-cache-tuning` → added `_headers` for cache control

---

## 📅 Timeline Updates

Use tags that reflect editorial scope:
- `v2.0-timeline-expansion` → added new grouped sections or cases
- `v2.1-entry-refinement` → updated language or metadata for clarity
- `v2.2-legal-status-update` → reflects new developments in a case

---

## 🧼 Editorial Hygiene & Infrastructure

Use tags to signal technical polish and contributor clarity:
- `v1.0-rss-ready` → initial validator-compliant feed
- `v1.1-contributor-docs` → added `CONTRIBUTING.md`, onboarding notes
- `v1.2-badge-signaling` → added visual indicators of validator compliance
- `v1.3-netlify-sync` → updated repo and deployment settings

---

## 🔁 Suggested Format

Use one of the following styles:
- Semantic: `vX.Y.Z-scope` (e.g. `v1.0.1-validator-fix`)
- Milestone: `vX.Y-scope` (e.g. `v2.0-timeline-expansion`)

Avoid:
- Unscoped tags like `v1.0-update`
- Redundant tags like `v1.0-final-final`

---

## 🧭 Tagging Workflow

1. Merge PR to `main`
2. Draft GitHub release with scoped tag
3. Include changelog in release description
4. Confirm footer auto-updates via GitHub API
5. Optionally update `RELEASE-README.md` with milestone summary

---
