# TODOs and Optional Enhancements

## 🛠️ Technical Enhancements

### RSS Generator

- [ ] Log malformed titles when date parsing fails
- [ ] Add `<language>` tag to RSS feed for completeness
- [ ] Validate RSS output with W3C Feed Validator
- [ ] Consider GitHub Actions for automated feed generation

### CSS Layout

- [ ] Review scroll offset behavior with dynamic headers
- [ ] Explore responsive tuning for `--scroll-offset` via media queries
- [ ] Document layout variables in a central `design.md` file

## 🐛 Bugs or quirks you notice but don’t want to fix immediately

## 🧠 Editorial notes or content refinements

- [ ] Add editorial notes to timeline entries for context

## 🧪 Ideas for future automation or testing

## 🌐 Social Media Metadata

- [x] Update social preview image with new filename to force cache refresh on X (Twitter)
- [ ] Monitor X cache behavior to confirm new image is picked up in public posts

---

Absolutely, Thomas! Here's a clean, modular Markdown version you can drop into your `TODO.md` for Iryna-Watch. It’s structured for clarity and future-proofing, with minimal disruption to your current layout.

---

## 🧭 TODO: Explore Smooth Responsive Navbar for Iryna-Watch

### Goal

Investigate replacing the generic built-in navbar with a smooth, scroll-reactive Bootstrap 5 version—without disrupting the current visual identity.

---

### ✅ Minimal Setup (No Node Required)

#### 1. **Include Bootstrap via CDN**

```html
<!-- In <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Before </body> -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

#### 2. **Basic Navbar Structure**

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-transparent fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Brand</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Features</a></li>
      </ul>
    </div>
  </div>
</nav>
```

#### 3. **Scroll-triggered Background Change**

```html
<script>
window.addEventListener('scroll', function () {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.classList.add('bg-dark');
    navbar.classList.remove('bg-transparent');
  } else {
    navbar.classList.add('bg-transparent');
    navbar.classList.remove('bg-dark');
  }
});
</script>
```

#### 4. **Smooth Transition Styling**

```css
.navbar {
  transition: background-color 0.3s ease;
}
```

---

### 🧠 Notes

- Uses Bootstrap’s built-in responsive collapse for hamburger menu.
- Scroll behavior is handled with vanilla JS—no dependencies.
- Easily themeable via `:root` variables and modular class overrides.
- Can be styled to match Iryna-Watch’s current palette and layout conventions.

---
