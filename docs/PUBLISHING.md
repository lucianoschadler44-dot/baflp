# Publishing Workflow

`scripts/build.sh` runs Quarto once and emits the website plus PDF, DOCX and EPUB into `build/`.
On push to `main`, GitHub Actions (`.github/workflows/build.yml`) renders and deploys the website
to GitHub Pages, served at **research.schadler.tech** (see `website/CNAME`). Nothing in `build/`
is committed — outputs are always regenerated.
