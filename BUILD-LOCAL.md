## 🛠️ Local Build Instructions (`BUILD-LOCAL.md`)

### Overview
This guide outlines the steps required to build and test the site locally before pushing to `dev`. It ensures that the RSS feed is up-to-date and that all assets are correctly referenced.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

---

### 2. Set Up Python Environment

Ensure you have Python 3 installed. Then install dependencies:

```bash
pip install beautifulsoup4
```

Or, if you use a `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 3. Run the RSS Generator

```bash
python scripts/rss-generator.py
```

- This script updates `rss.xml` in the root directory.
- Confirm that the file reflects the latest timeline entries.
- Check that `<lastBuildDate>` is current.

---

### 4. Verify Local Build

- Open `index.html` in a browser.
- Confirm:
  - Timeline renders correctly
  - RSS icon links to `./rss.xml`
  - Footer and navigation behave as expected

---

### 5. Commit Changes

```bash
git add rss.xml
git commit -m "Update RSS feed before dev push"
```

---

### 6. Push to `dev`

```bash
git push origin dev
```

---
