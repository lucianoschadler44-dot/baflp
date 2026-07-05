---
id: concept-0003
title: "Artificial Registry"
slug: artificial-registry
version: 0.2.0
status: draft
complexity: beginner
authority: chief-research-architect
summary: >
  The authoritative record establishing the existence and status of artificial legal persons.
relations: { depends-on: [], related-to: [concept-0006], supersedes: null }
lenses: { citizen: true, professional: true, researcher: true }
references: []
created: 2026-06-27
updated: 2026-07-05
---

## In one sentence (citizen)
A public list, kept by an authority, shows which artificial companies exist and who answers for
them. If it is not on the list, it does not exist as a legal person.

## In practice (professional)
The registry holds the entity's constitution, declared operator and ultimate beneficial owners,
status (active, suspended, dissolved), continuity events and audit hooks. Public access lets any
counterparty verify who they face.

## Formal definition (researcher)
The authoritative, tamper-evident record establishing the existence, status, attributes and
responsible parties of artificial legal persons; the trust anchor on which identity
(`concept-0001`), continuity (`concept-0002`) and liability (`concept-0005`) depend.

## Example
Argentina's 2026 bill pairs legal personality for AI-run companies with mandatory disclosure of
ultimate beneficial owners — a registry function.

## Counterexample
A private spreadsheet of AI agents: informative, but with no legal force and no duty to be
accurate.

## Frequently misunderstood
"Registry" does not mean blockchain. The defining properties are authority, auditability and
tamper-evidence — the technology is an implementation choice.

## Practical implications
Registry quality decides whether the beneficiary of an artificial person can be traced — the
direct answer to the "responsibility vacuum" critique.

## Visual
Registry lifecycle diagram (planned).

## See also
`concept-0006` (Audit) · `concept-0005` (Liability)
