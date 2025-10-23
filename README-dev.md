# Iryna Timeline (Dev Branch)

This branch contains editorial scaffolding for the Iryna timeline project. All changes here are staged for review before public release.

### 🧾 Summary

- Timeline / RSS updates and code hygiene are tested in `dev`. This includes automated code review and manual functionality tests.
- Feature or experimental changes are developed in their own branch before merging into `dev`.

---

### 🛠️ Release Updates and Testing

- Most releases involve timeline and RSS updates or code hygiene.
- For recent changes and validation history, see [commit.md](./commit.md).
- Major rewrites or logic changes will be noted here. Otherwise, review the commit log for changes.

---

## 🧠 Editorial Logic

This timeline prioritizes clarity, dignity, and restraint. Filings are tagged to reflect both legal classification and narrative significance:

- `motion`: High-impact procedural filings, including those that drew public scrutiny (e.g. medical evaluations)
- `procedural-motion`: Routine filings such as continuances or scheduling orders; hidden by default to reduce visual clutter

The toggle interface allows users to reveal procedural depth without overwhelming the default view.

---

## 🧠 Contribution Workflow

We use a principled pull request process to preserve editorial restraint and technical clarity.

- All changes are made in the `dev` branch and tested via GitHub Pages.
- Once ready, a [pull request](https://github.com/CharlieFox84/irynawatch/compare/main...dev) is opened from `dev` to `main`.
- Merging triggers Netlify auto-deploy to [irynawatch.netlify.app](https://irynawatch.netlify.app/).

📄 See our [Pull Request Template](./PULL_REQUEST_TEMPLATE.md)

---

## 🧪 Testing Before PR

Before submitting a pull request to `main`, please follow the steps in [`TESTING.md`](./TESTING.md).

---

## 🧭 Recommended Sequence
- ✅ Open PR from dev to main
- ✅ Merge PR and let Netlify deploy main
- ✅ Confirm deploy success (Netlify dashboard or site check)
- ✅ Create GitHub release tag (e.g. v1.0.0)
- ✅ Verify that your site reflects the tag and date correctly

---

## 🧾 Editorial Notes

- All content is handled with restraint and respect  
- No public sourcing until verified and approved

---
![HTML/CSS/JS](https://badgen.net/endpoint/https://charliefox84.github.io/Iryna-Validation/html.json)
![RSS Feed](https://badgen.net/endpoint/https://charliefox84.github.io/Iryna-Validation/rss.json)

---

### 🏷️ Commit Message Tags

| Tag           | Purpose                                                                 |
|---------------|-------------------------------------------------------------------------|
| `Timeline:`   | Updates to timeline entries or editorial content                        |
| `RSS:`        | Changes to RSS feed structure, content, or syndication logic            |
| `Infra:`      | Infrastructure-level updates (e.g., links, monitoring, layout scaffolding) |
| `Style:`      | Visual or CSS changes that affect presentation but not content          |
| `Meta:`       | Metadata updates (e.g., descriptions, SEO, OpenGraph, canonical links)  |
| `Docs:`       | Changes to documentation, README, or internal notes                     |
| `Dev:`        | Tooling, scripts, automation, or developer workflow improvements        |

---

### 🏷️ Example Usage

```
Infra: Add direct docket link to footer
Timeline: Draft entry for protective order motion
RSS: Fix date formatting in feed items
Dev: Refactor changelog script for clarity
```
