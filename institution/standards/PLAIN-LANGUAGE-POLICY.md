# Plain Language Policy (ADR-0001 §5 — mandatory)

Every official publication must be understandable by an educated reader. Every canonical concept
must provide, in one single source file: an academic definition, a professional explanation, a
plain-language explanation (citizen lens), an example and a visual.

Enforcement: the CI readability check (Phase 3) scores the citizen lens of every concept; text
above the target grade level flags the build. Accessibility is tested, not hoped for.

Editing rule (Chief Editor decision, 2026-06-28): lenses and cards are auto-drafted by the
multi-AI pipeline; humans edit CONTENT files afterwards. Humans never patch the ENGINE
(scripts/, generators, build config) to fix one piece of content.
