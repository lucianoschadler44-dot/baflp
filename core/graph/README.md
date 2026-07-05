# graph

> Part of **BAFLP** — layer scaffolding created by ADR-0001 Phase 1.

## Purpose
Knowledge dependency graph: nodes = objects, edges = relations/references.

## Contents
graph.json (generated) · schema.json.

## Dependencies
Built by scripts/graph-build.py (Phase 3); consumed by explorer + CI impact.

## Future evolution
RDF export; adjacency precompute at scale.
