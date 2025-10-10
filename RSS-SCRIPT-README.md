## 📜 `RSS-SCRIPT-README.md`

### Overview

This folder contains utility scripts used to generate dynamic assets for the Iryna Watch timeline. These scripts are designed with editorial restraint, technical hygiene, and contributor clarity in mind.

---

### 🐍 `rss-generator.py`

Generates a compliant `rss.xml` feed from the timeline content in `index.html`.

#### Features

- Parses timeline cards and groups them by editorial category (`case`, `incident`, `community`)
- Sorts entries by recency within each category
- Extracts and sanitizes titles, descriptions, and dates
- Outputs a validator-compliant RSS feed with:
  - Escaped ampersands
  - Sanitized GUIDs
  - `isPermaLink="false"` for non-URL identifiers
  - Atom self-reference tag
  - Graceful fallback for malformed or future dates

#### Usage

```bash
python rss-generator.py
```

This will regenerate `rss.xml` in the root directory.

#### Dependencies

- `beautifulsoup4`
- Python 3.7+

Install with:

```bash
pip install beautifulsoup4
```

---

### 🧼 Editorial Hygiene Notes

- Ampersands (`&`) are replaced with “and” for XML safety
- Brackets (`[ ]`) are replaced with parentheses in GUIDs
- `<em>` tags are stripped from descriptions to preserve RSS validity
- Future dates are allowed but fallback logic ensures feed integrity

---

![RSS Feed: Validator Compliant](https://img.shields.io/badge/RSS%20Feed-Validator%20Compliant-brightgreen?style=flat-square)