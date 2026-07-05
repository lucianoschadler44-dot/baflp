---
id: concept-0004
title: "Governance"
slug: governance
version: 0.2.0
status: draft
complexity: intermediate
authority: chief-research-architect
summary: >
  How decisions are made, constrained and attributed within an artificial legal person.
relations: { depends-on: [], related-to: [concept-0006, concept-0005], supersedes: null }
lenses: { citizen: true, professional: true, researcher: true }
references: []
created: 2026-06-27
updated: 2026-07-05
---

## In one sentence (citizen)
Clear rules say how the artificial company makes its choices and who wrote those rules. Good rules
are public, so anyone can check them.

## In practice (professional)
Governance is encoded in the entity's constitution: decision rights, operating rules, escalation
and override points, and who may change the rules. Declared governance is what courts and
counterparties measure conduct against.

## Formal definition (researcher)
The structure of decision-making authority, constraints and attribution within an artificial legal
person, fixed in its constitution, observable through audit (`concept-0006`) and relevant to the
allocation of liability (`concept-0005`).

## Example
An AI newsroom where an editor-in-chief process selects stories each hour under publicly declared
editorial rules — transparency, verifiability, open corrections.

## Counterexample
An autonomous agent with no declared rules and no accountable rule-setter: whatever it does, no
standard exists to judge it by.

## Frequently misunderstood
Governance is not the same as human supervision. An entity can be well governed with little human
intervention — if its rules are declared, followed and auditable.

## Practical implications
Declared governance turns "the AI decided" into "the entity acted within (or outside) its
constitution" — a question courts can actually adjudicate.

## Visual
`diagrams/mermaid/governance-flow.mmd`.

## See also
`concept-0006` (Audit) · `concept-0005` (Liability)
