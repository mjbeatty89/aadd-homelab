# Repo Scope

> This repository is the homelab knowledge base, not the default home for application code.

## What Belongs Here
- Durable homelab documentation.
- Host, service, network, and runbook notes.
- LLM wiki schemas, templates, and agent operating rules.
- Architecture decisions and incident records.
- Project notes when they document the homelab itself or how agents should work with it.

## What Does Not Belong Here
- Full application source for unrelated projects.
- Large media collections, proposal assets, or personal image dumps.
- Secrets, credentials, tokens, private keys, or `.env` files.
- Local plugin caches, generated embeddings, and workstation-only state.

## How To Use This Repo As A Guideline
- It is fine to point other projects or agents at this repo as a reference model.
- Treat it as the operating manual and architectural memory for em0lab.
- If another project needs to borrow structure, copy the conventions rather than merging that project's code into this repo.
- If a project needs to link back here, add a project note or ADR that describes the relationship.

## Recommended Pattern
1. Keep the implementation in its own repo.
2. Keep the durable operational knowledge here.
3. Link the two with project notes, runbooks, ADRs, and source-of-truth references.

## Gastown Note
If `gastown` used this repo as a guideline, that is fine.
If `gastown` starts adding substantial app code or unrelated artifacts here, we should move that code into its own repo and keep only the knowledge/relationship note here.

## Related
[[Home]] · [[Projects/LLM Wiki Second Brain]] · [[Schemas/LLM Wiki Schema]]

