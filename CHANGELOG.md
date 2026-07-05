# Changelog

All notable changes to the BAFLP are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/).

## [Unreleased]

## [0.4.1] - 2026-07-05
### Fixed
- CI: Pages deployments now queue instead of cancelling; manifesto bot triggers site rebuild after committing.

## [0.4.0] - 2026-07-05
### Added
- Public Consultation: 12 trilingual questions as GitHub ballots (reactions = votes), live-results page.
- Living Manifesto: axioms + quorum-gated majority positions, recompiled daily by repo automation.
### Changed
- Simulator repositioned as plain-language Compliance Checklist with full-flow answers.

## [0.3.0] - 2026-07-05
### Added
- AI-readability layer: llms.txt + llms-full.txt (llmstxt.org), "AI" portal page with ready prompts (PT/ES/EN), Open Graph/Twitter cards, GitHub topics.
### Fixed
- Folder index convergence + generated glossary page (if pending).

## [0.2.3] - 2026-07-05
### Fixed
- Site render: canonical directory render list; slim site workflow (no TinyTeX/PDF in Pages build) + artifact sanity check.

## [0.2.2] - 2026-07-05
### Fixed
- CI: empty YAML frontmatter fields (category/author) removed; permanent yaml-empty test added to CI and validate.sh.

## [0.2.1] - 2026-07-05
### Fixed
- CI: TinyTeX made non-blocking; removed placeholder CSL from the render pipeline.

## [0.2.0] - 2026-06-28
### Added
- Institutional portal (trilingual landing EN/ES/PT, About, generated Glossary).
- Six-layer scaffolding (institution, observatory ×9, public-experience) per ADR-0001.
- Knowledge engines: dependency graph, impact analysis, auto-glossary, readability check.
- Case Study 0001 (Argentina) fact-verified and moved to observatory/argentina.
### Added
- Repository bootstrap: full directory architecture, READMEs, governance, knowledge-object
  templates, Quarto build pipeline, CI/CD, translation scaffolding (es-AR, pt-BR).

## [0.1.0] - 2026-06-27
- Initial infrastructure (engineering only — no legal doctrine yet).
