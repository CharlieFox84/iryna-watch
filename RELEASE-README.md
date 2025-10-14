# RELEASE-README

This file documents the release process and editorial standards for the `iryna-watch` project. It reflects a commitment to clarity, dignity, and technical transparency.

---

## 🏷️ Current Release

**Tag**: `v1.0-rss-ready`  
**Date**: October 9, 2025  
**Status**: Production-ready  
**Live site**: [https://irynawatch.netlify.app](https://irynawatch.netlify.app)

---

## 📦 Release Contents

- ✅ Validator-compliant RSS feed (`rss.xml`)
- ✅ RSS generator script (`rss-generator.py`)
- ✅ Editorial hygiene: ampersand sanitization, scoped GUIDs, tag stripping
- ✅ `<link rel="alternate">` for feed discoverability
- ✅ RSS documentation (`RSS-SCRIPT-README.md`)
- ✅ RSS badge added to main `README.md`
- ✅ Netlify deployment confirmed
- ✅ Mobile-first layout validated
- ✅ Cache-control headers for respectful freshness

---

## 🔄 Release Workflow (example)

1. **Merge PR to `main`**
   - Title: `Sync dev to main: finalize RSS feed and editorial infrastructure`
   - Description includes validator fixes, documentation, and deployment status

2. **Create GitHub Release**
   - Navigate to the repo → “Releases” → “Draft a new release”
   - Tag: `v1.0-rss-ready`
   - Target: `main`
   - Description: See above

3. **Auto-update Last updated**
   - script fetches latest release tag via GitHub API
   - Displays: `Last updated: DATE RELEASE-NUMBER`

4. **Deploy via Netlify**
   - Repo: `charliefox84/iryna-watch`
   - Branch: `main`
   - Cache headers set via `_headers` file:
     ```plaintext
     /rss.xml
       Cache-Control: public, max-age=86400, must-revalidate
     ```

---

## 🧭 Editorial Philosophy

This project centers dignity, restraint, and factual clarity. All releases reflect:
- Respectful handling of trauma and legal documentation
- Transparent infrastructure and contributor onboarding
- Modular, auditable systems for principled participation

---

## 🛠️ Next Steps

- Tag future releases (`v1.0.1`, `v1.1`, etc.) as infrastructure evolves
- Scaffold `CONTRIBUTING.md` for onboarding
- Expand glossary and grouped timeline modules
- Invite principled participation via badges and documentation

---
