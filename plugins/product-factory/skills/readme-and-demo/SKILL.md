---
name: readme-and-demo
description: Use when a project is ready to release. Writes a README in the awesome-readme pattern and records a scripted demo (MP4 and GIF) with Playwright or vhs.
---

# README and demo

## README pattern (from the READMEs collected in awesome-readme)
1. Name and one line of value (what it does, for whom).
2. **Demo GIF at the top** (10 MB or less, about 800 px wide), a live demo link, and badges (CI,
   licence, version).
3. Why it exists (the problem, in one short paragraph).
4. Features (5 to 7 bullets).
5. Quick start that works copy-pasted on a fresh machine.
6. Usage examples or screenshots, tech stack, roadmap, contributing, licence.

Also set the repo's description, topics (5 to 10) and homepage. They drive GitHub search.

## Demo video
- Script the journey with Playwright (`recordVideo` on the browser context) against a preview URL:
  60 seconds or less, the activation path only, realistic sample data, no personal data.
- Convert with ffmpeg: MP4 (H.264, `-preset veryfast`) for the release, and a GIF via
  `palettegen` and `paletteuse` for the README. For terminal tools, use `charmbracelet/vhs`.
- Store `docs/demo.gif` in the repo and attach the MP4 to the GitHub release.
- Captions: short, present tense, one per step.

## Exit check
A newcomer can understand the project from the first screen of the README and run it with the
quick start. The GIF renders on GitHub and all links work.

## Sources
- awesome-readme: https://github.com/matiassingers/awesome-readme
- Playwright videos: https://playwright.dev/docs/videos
- vhs: https://github.com/charmbracelet/vhs
