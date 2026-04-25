# Repository Resync and Fresh Start

## Purpose

This README explains two common workflows when your local copy and GitHub diverge or when you want a clean repository to start from: (A) resyncing when GitHub is newer than your local copy, and (B) creating a fresh repo and archiving or replacing an out‑of‑date repository. Use this as a quick, copy‑ready reference to preserve history, keep CI/CD and Netlify working, and avoid accidental data loss.

---

## Quick decisions

Keep full history and metadata → use a mirror clone and push refs to the new repo.
Keep only current files → create a new repo and import the working tree or use an orphan branch.
Preserve issues and PRs → archive the old repo rather than delete; export issues if you must delete.

---
Resync When GitHub Is Newer
Goal: make your local copy match the remote safely.
Fetch and inspect remote changes
git fetch origin
git status
git log --oneline origin/main..main

If you want to keep local commits, rebase or merge
git checkout main
git pull --rebase origin main

## or

git merge origin/main

If local is stale and you want the exact remote state
git fetch origin
git reset --hard origin/main

Warning: git reset --hard discards local uncommitted changes. Back up any work first (stash or copy files).
Preserve local branches
git push origin my-branch

## or create patches

git format-patch origin/main..my-branch

---
Start Fresh by Cloning a New Repo
Goal: create a clean repository with current files while preserving or discarding history as desired.
Create the new repo on GitHub (web UI or CLI).
Clone the new repo locally
git clone git@github.com:org/new-repo.git
cd new-repo

Import current site files from the old repo
Working tree only (no history)
cp -R ../old-repo/* .
git add .
git commit -m "Initial import from old-repo at YYYY-MM-DD"
git push origin main

Single clean commit using an orphan branch
git checkout --orphan clean-start
git rm -rf .
cp -R ../old-repo/* .
git add .
git commit -m "Clean start: import current site files"
git push origin clean-start:main

If you need full fidelity of tags and refs
git clone --mirror git@github.com:org/old-repo.git
cd old-repo.git
git remote add new git@github.com:org/new-repo.git
git push --mirror new

---

## Preserve Releases CI and Deploys

- Releases and assets are not moved by a simple clone. Download release assets from the old repo and reattach them to the new repo if needed.
- CI workflows and secrets must be recreated in the new repo (GitHub Actions, CircleCI, etc.). Export workflow files and reconfigure secrets.
- Netlify: update the site to point to the new repo or create a new Netlify site and copy build settings, environment variables, and deploy hooks. Confirm the custom domain and DNS settings.
- Tags: push tags explicitly with git push --tags origin.
- Archive versus Delete
- Archive the old repo when you want a reversible, read‑only record. Add a short README pointing to the new repo.
- Delete only after exporting issues, PRs, and releases you need. Deletion is permanent.

---

Quick checklist before switching
Back up release assets and tags.
Export or copy important issues and PRs if needed.
Recreate CI workflows and secrets in the new repo.
Update Netlify build settings and environment variables.
Add a README redirect in the old repo and archive it.
Verify the new repo deploys and production matches expected output.
Announce the change to collaborators.
Old repo README snippet

## Archived Repository

This repository has been replaced by: https://github.com/ORG/NEW-REPO

The new repo contains the current site and active development. This archive is read-only.

---

## Commands Reference

- Mirror clone preserve refs and tags: git clone --mirror git@github.com:org/old-repo.git
- Fresh clone: git clone git@github.com:org/new-repo.git
- Create orphan branch: git checkout --orphan clean-start
- Reset local to remote: git fetch origin && git reset --hard origin/main
- Push tags: git push --tags origin

---
