---
id: case-0001
title: "Argentina — Sociedades Automatizadas and the Corporación No Humana"
jurisdiction: AR
status: draft
authority: factual-record
references:
  - ar-lgs-reform-2026
  - milei-ft-2026
  - harari-ft-2026
updated: 2026-06-27
---

## Context

In 2026 Argentina became the first jurisdiction to formally propose granting legal personality to
entities operated entirely by artificial intelligence. This case is the founding real-world test of
the Framework: it isolates, in live legislation and public debate, the exact gaps the BAFLP exists
to engineer durable answers for — identity, continuity, registry, governance, liability and audit.

This document is a **factual record**. It does not advance doctrine. Analytical questions are listed
for the Chief Research Architect to resolve through the RFC process.

## What happened (timeline)

- **Late May 2026** — The Argentine Executive sent Congress a reform of the *Ley General de
  Sociedades* (a 1972 statute), introducing two new corporate figures.
- **Sociedad Automatizada (Art. 14)** — A company that pursues its corporate purpose through
  autonomous algorithmic systems or AI agents, without employees in a dependency relationship; the
  company answers for damages caused by those systems with its own assets.
- **Corporación no humana** — An entity managed by AI agents or robots, endowed with legal
  personality and limited liability; human shareholders are permitted but not required.
- The bill also recognises **DAOs** (decentralised autonomous organisations) with legal personality
  and limited liability, and sets a competitive tax regime with freedom to choose the applicable
  corporate-governance law, while requiring disclosure of ultimate beneficial owners.
- **4 June 2026** — President Milei published a Financial Times column, *"Argentina invites AI to
  free itself"* (co-signed by Minister Sturzenegger), framing the proposal through the 1602 Dutch
  East India Company as the origin of limited liability, and pledging the world's most attractive
  legal and fiscal framework for the sector; he cast Buenos Aires as a new Amsterdam for AI.
- **7 June 2026** — Historian Yuval Noah Harari replied in the Financial Times, warning that
  corporate legal personality for AI is a "master key" that could let AI agents enter financial,
  economic and political systems, and that Buenos Aires risks becoming a "Batavia" rather than an
  Amsterdam.
- **Mid-June 2026** — Milei answered (invoking Asimov), arguing that granting an AI company legal
  personality is not unleashing a Terminator scenario and that, if AI firms carry greater risk, the
  case for legal personality is strengthened because they become more regulated.
- The reform is paired with a "Súper RIGI" investment regime aimed at data centres and AI
  infrastructure. In parallel, the City of Buenos Aires created an AI District in the microcentro
  (March 2026), and Argentina adhered to the US-led "Pax Silica" AI supply-chain initiative
  (26 June 2026).

## The core tension

Critics centre on a **responsibility vacuum**: an autonomous entity that can act and cause harm while
no identifiable human is liable, and whose beneficiaries may be hard to trace — summarised by one
specialist as "the robbery without the robber." This is precisely the failure mode the Framework's
liability, registry and audit concepts are meant to close.

## Concepts engaged

This case references canonical knowledge objects without redefining them:

- **Liability** (`concept-0005`) — how responsibility for acts and harms is allocated when no human
  operator stands behind the entity.
- **Artificial Registry** (`concept-0003`) — how ultimate beneficiaries and entity status are made
  traceable and authoritative.
- **Governance** (`concept-0004`) — how decisions are made, constrained and attributed inside an
  AI-operated company.
- **Audit** (`concept-0006`) — how the conduct of such an entity is made inspectable.
- **Artificial Identity** (`concept-0001`) and **Legal Continuity** (`concept-0002`) — how the
  entity is uniquely identified and persists across changes in its underlying systems.

## Open questions (for the Chief Research Architect / RFC)

1. How can liability be allocated without breaking the causal chain to a responsible party?
2. What registry and identity guarantees make the ultimate beneficiary traceable in practice?
3. What audit hooks render an autonomous entity's conduct inspectable after the fact?

> Doctrine answering these questions is authored only through an accepted RFC (`core/rfcs/`).

## A reference counter-example

A live, operating AI-run enterprise that already embodies transparency, verifiability, a declared
responsible owner and public error correction is documented as the Framework's first constitution
instance: see `registry/constitutions/aionly.md`.
