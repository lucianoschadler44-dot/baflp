---
id: case-0001
title: "Argentina — 'Sociedades Automatizadas' and the legal personhood of AI-run companies"
jurisdiction: Argentina
status: draft
references:
  - ar-lanacion-2026-ley-sociedades
  - ar-infobae-2026-sociedades-ia
  - ar-perfil-2026-ley-sociedades
  - ar-chequeado-2026-dao-explicador
  - ar-unlp-sociedades-automatizadas
  - ba-herald-2026-milei-harari
updated: 2026-06-27
---

> Factual case record approved by the Chief Editor (decision-log: ED-0001). This document
> reports a real-world legislative debate; it does **not** define BAFLP doctrine. Concepts are
> engaged by reference to their canonical ids — their meaning is fixed only in `core/concepts/`
> through accepted RFCs.

## Context

Argentina's company law is built on the *Ley General de Sociedades* (LGS, Ley 19.550) and, since
2017, the lightweight *Sociedad por Acciones Simplificada* (SAS, Ley 27.349). Both presuppose
human members behind the legal person. The reform debated in 2026 tests whether that presupposition
can be dropped — i.e. whether an entity operated entirely by algorithms or AI agents can itself hold
full legal personality. This is the canonical real-world stress test the Framework was built to
analyse (see `research/case-studies/README.md`).

## What happened

- In **May 2026** the national government (Milei administration) submitted to Congress a bill
  reforming the company-law regime, introducing two new figures: **Sociedades Automatizadas**
  (automated companies) and **Organizaciones Autónomas Descentralizadas / DAOs**.
- A **Sociedad Automatizada** is defined as a company that develops its corporate purpose through
  autonomous algorithmic systems or AI agents, **without requiring employees** for ordinary
  operation. The proposal grants it full legal personality, capacity to act with third parties, and
  limited liability — **responding with its own assets** for damages caused by its autonomous
  systems.
- Formal requirements reported for the figure: the **declaration of automation must appear in the
  statute**, and the company **name must include the word "Automatizada."**
- **DAOs** are treated as a distinct figure: rules codified in smart contracts and registered on
  blockchain, with power distributed among token holders — contrasted with the centralised
  algorithmic control of a Sociedad Automatizada.
- The proposal triggered a high-profile public clash: President **Javier Milei** (who had argued in
  a *Financial Times* column for an AI framework without prior regulation) versus historian
  **Yuval Noah Harari** and Microsoft AI CEO **Mustafa Suleyman**, who warned that granting legal
  personhood to autonomous algorithms without a human in the loop erodes accountability — "you
  cannot jail an AI." Milei replied that legal personhood for AI agents is "not launching the
  Judgment Day of Terminator."
- **As of June 2026 the bill is under congressional debate**; this record is a living document to be
  updated as the case develops (enactment, amendments, regulatory decrees, first registered entity).

## Concepts engaged

This case touches the following canonical concepts (definitions pending in `core/concepts/`):

- **Artificial Identity** (`concept-0001`) — the mandatory "Automatizada" naming and the statutory
  declaration of automation as identity markers.
- **Artificial Registry** (`concept-0003`) — registration of an automated entity in the companies
  registry; the blockchain-as-registry question raised by the DAO figure.
- **Governance** (`concept-0004`) — corporate purpose executed by autonomous algorithmic systems
  with no mandatory human in the loop.
- **Liability** (`concept-0005`) — the bill's core mechanism: the entity responds with its own
  assets; the Harari/Suleyman accountability critique.
- **Legal Continuity** (`concept-0002`) — an entity with no employees and algorithmic operation
  raises questions of persistence, dissolution and succession.
- **Audit** (`concept-0006`) — what verification of the autonomous systems is required before and
  during the entity's life.

## Analysis

(pending — analysis of how BAFLP's model law would treat this case is authored only through an
accepted RFC; this section is intentionally left as a sourced factual record, not doctrine.)

## Open questions

1. Does "responds with its own assets" create a genuine liability shield, or merely relocate
   liability to the entity's capital while leaving principals reachable (piercing)?
2. Where is the human in the loop located — at incorporation, at governance, or nowhere — and does
   the statute fix accountability for harms caused autonomously?
3. How does the registry verify and audit the "autonomous algorithmic system" at registration, and
   on what cadence thereafter (`concept-0003`, `concept-0006`)?
4. Is the Sociedad Automatizada / DAO distinction durable, or do hybrid forms collapse it?
5. How would BAFLP's model law classify this figure relative to its own taxonomy? (RFC required.)
