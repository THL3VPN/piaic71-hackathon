---
id: 0001
title: spec-meta-specify
stage: general
date: 2025-12-10
surface: specs
model: gpt-5
feature: none
branch: 001-interactive-cli-ux
user: aie
command: manual (meta-spec creation for /specs/specify.md)
labels: [spec-kit, governance]
links:
  spec: specs/specify.md
  ticket: null
  adr: null
  pr: https://github.com/THL3VPN/piaic71-hackathon/pull/7
files:
  - path: specs/specify.md
    note: add meta-spec defining spec organization, priority, and agent usage
tests:
  - status: not run
    note: documentation-only change
---

## Prompt

User provided full content for `/specs/specify.md` (meta-specification): describe Spec-Kit organization, rule priority, agent usage, phases, referencing rules, JWT/auth rules, and permissions. Must not assume a specific path for the Constitution file.

## Response snapshot

Created `/specs/specify.md` with the supplied meta-spec text, defining spec structure, priority order, agent responsibilities, enforcement of spec-driven development, JWT/auth rules for Phase II, and edit policy.

## Outcome

- ✅ Impact: Specs directory now has authoritative meta-spec for Spec-Kit use and rule priority.
- 🧪 Tests: not run (doc-only).
- 📁 Files: specs/specify.md added.
- 🔁 Next prompts: use this meta-spec when generating/consuming specs, plan, and tasks.
- 🧠 Reflection: Scripted PHR failed due to repo root mismatch; created PHR manually under history/prompts/general.
