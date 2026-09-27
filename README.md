# mininglife7-dev.github.io

HaanJi static site on GitHub Pages: https://mininglife7-dev.github.io/

Source of truth is `/workspace/receptionist-ai/site/` on the build box. `.github/workflows/sync.yml` mirrors every file in `files.txt` from the URL in `source_url.txt` (the box's current site tunnel) into the repo root and commits it. To re-sync: update `source_url.txt` or run the workflow manually.
