---
id: concept-0002
title: "Legal Continuity"
slug: legal-continuity
version: 0.2.0
status: draft
complexity: intermediate
category:
authority: chief-research-architect
summary: >
  How an artificial legal person persists across changes in its underlying systems.
relations: { depends-on: [concept-0001], related-to: [concept-0003], supersedes: null }
lenses: { citizen: true, professional: true, researcher: true }
references: []
created: 2026-06-27
updated: 2026-07-05
---

## In one sentence (citizen)
The company stays the same person under the law, even when its software is updated or replaced.
Its duties and its rights do not vanish with an update.

## In practice (professional)
Continuity rules define which events preserve the entity (model upgrades, infrastructure
migration, operator succession) and which create a new one (unregistered forks). Continuity events
are recorded in the registry so counterparties can verify succession.

## Formal definition (researcher)
The property by which an artificial legal person's rights, obligations and identity persist across
modifications of its operating models, code or infrastructure, conditional on registry-recorded
continuity events and the identity guarantees of `concept-0001`.

## Example
The AI-run enterprise swaps its language model for a newer one; existing contracts, debts and
licenses remain binding on the same legal person.

## Counterexample
Cloning an AI system into a new, unregistered entity to escape debts: the clone is not the
original person and gains none of its rights — and the original's obligations remain.

## Frequently misunderstood
Continuity is legal, not technical. A full rewrite can preserve the person; an identical copy can
fail to.

## Practical implications
Without continuity rules, obligations could be escaped by "re-incorporating" after every harm —
the loophole regulators most fear.

## Visual
Timeline diagram of continuity events (planned).

## See also
`concept-0001` (Artificial Identity) · `concept-0003` (Artificial Registry)
