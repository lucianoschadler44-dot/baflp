---
id: concept-0006
title: "Audit"
slug: audit
version: 0.2.0
status: draft
complexity: beginner
authority: chief-research-architect
summary: >
  How the conduct of an artificial legal person is made inspectable and accountable.
relations: { depends-on: [], related-to: [concept-0004], supersedes: null }
lenses: { citizen: true, professional: true, researcher: true }
references: []
created: 2026-06-27
updated: 2026-07-05
---

## In one sentence (citizen)
Everything important the company does must leave a record. Anyone with the right to check can see
what happened and why.

## In practice (professional)
Audit hooks include decision and action logs, provenance of outputs, labeling of AI-produced
content, public and dated corrections, and inspection rights for authorities and counterparties.

## Formal definition (researcher)
The set of mechanisms rendering an artificial legal person's conduct inspectable ex post —
records, provenance, disclosure and correction procedures — sufficient for adjudication and for
enforcing the entity's declared governance (`concept-0004`).

## Example
A newsroom that publicly retracts factual errors with date and explanation, never editing them
away in silence: its conduct leaves a verifiable trail.

## Counterexample
A system whose decisions cannot be reconstructed after the fact: no trail, no adjudication, no
accountability.

## Frequently misunderstood
Audit is not model explainability. It concerns records of the entity's conduct, not the neural
internals of its software.

## Practical implications
Audit is what makes liability adjudicable: without a trail, even a perfect liability regime has
nothing to act on.

## Visual
Audit-trail diagram (planned).

## See also
`concept-0004` (Governance) · `concept-0005` (Liability)
