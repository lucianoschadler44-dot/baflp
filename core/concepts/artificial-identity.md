---
id: concept-0001
title: "Artificial Identity"
slug: artificial-identity
version: 0.2.0
status: draft
complexity: beginner
category:
authority: chief-research-architect
summary: >
  How an artificial legal person is uniquely and persistently identified.
relations: { depends-on: [concept-0003], related-to: [concept-0002], supersedes: null }
lenses: { citizen: true, professional: true, researcher: true }
references: []
created: 2026-06-27
updated: 2026-07-05
---

## In one sentence (citizen)
An artificial company needs one name and one number that never change. That way, everyone always
knows exactly who they are dealing with.

## In practice (professional)
Identity is the set of registry-anchored attributes — legal name, registration number, declared
operator, cryptographic keys where used — that individuate the entity in contracts, court filings
and service of process. It must survive software changes and vendor swaps.

## Formal definition (researcher)
The persistent, verifiable set of attributes that individuates an artificial legal person across
time and substrate changes, anchored in an authoritative registry (`concept-0003`) and preserved
under the continuity rules of `concept-0002`.

## Example
A newsroom operated entirely by AI keeps the same registration identity even after its underlying
models are replaced; its contracts and bylines remain attributable to the same legal person.

## Counterexample
An anonymous autonomous agent with no registered identity: capable of acting, impossible to sue,
serve or hold to account.

## Frequently misunderstood
Identity is not the software. The model can be rewritten entirely; the legal person — and its
obligations — remain the same if continuity rules are met.

## Practical implications
Without stable identity there is no valid contracting party, no addressee for liability and no
subject for audit. Identity is the entry ticket to legal personhood.

## Visual
See `diagrams/mermaid/governance-flow.mmd` (registry lifecycle diagram planned).

## See also
`concept-0003` (Artificial Registry) · `concept-0002` (Legal Continuity)
