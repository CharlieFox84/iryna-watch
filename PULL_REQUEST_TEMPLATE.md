# IrynaWatch Pull Request

## 🧾 Summary
Brief description of the changes introduced in this PR. Include context, intent, and any relevant editorial or technical notes.

## 🧠 Editorial Notes
- Maintains restraint and factual clarity.
- Updates grouped sections, glossary modules, or procedural cards as needed.
- Preserves dignity in presentation and avoids sensationalism.

## 🛠 Technical Notes
- Modularized CSS/JS or refined infrastructure.
- Cleaned config, updated README, or adjusted Netlify settings.
- GitHub Pages preview available via `dev` branch.

## 🚀 CICD Workflow Reference

### Development Branch (`dev`)
- All updates—editorial, CSS/JS, infrastructure—are made here.
- GitHub Pages is configured to build from `dev` for live testing.

### Testing & Review
- Visual and editorial checks are performed via GitHub Pages.
- Procedural cards and hidden tags allow for quiet iteration.

### Merge to Production (`main`)
- Once tested, a pull request is opened from `dev` to `main`, documenting the changes.
- The PR is reviewed and merged with a clean commit history.
- GitHub syncs the updated `main` branch.

### Netlify Auto-Deploy
- Netlify is linked to the `main` branch.
- Every push triggers a fresh build and deploy to [irynawatch.netlify.app](https://irynawatch.netlify.app/)
- Public-facing site updates automatically, preserving editorial restraint and technical polish.

---
