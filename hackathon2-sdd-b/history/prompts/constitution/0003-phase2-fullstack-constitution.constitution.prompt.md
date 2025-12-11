---
id: 0003
title: phase2-fullstack-constitution
stage: constitution
date: 2025-12-10
surface: governance
model: gpt-5
feature: none
branch: 001-interactive-cli-ux
user: aie
command: manual (gh pr context) – SpecKit template path unavailable from parent repo root
labels: [governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: https://github.com/THL3VPN/piaic71-hackathon/pull/7
files:
  - path: .specify/memory/constitution.md
    note: bumped to v2.0.0 for Phase II full-stack rules and stack constraints
tests:
  - status: not run
    note: documentation-only change
---

## Prompt

This document defines the governing rules for Phase II of the hackathon-todo project. The Constitution must include:
1. Purpose of Phase II: Transform the Phase I console todo app into a full-stack multi-user web application.
2. Enforce spec-driven development: Specs in /specs are the source of truth. Codex agents must always follow constitution.md, plan.md, tasks.md, specs/*; no implementation may contradict the Constitution.
3. Required Tech Stack: Frontend: Next.js 16+ (App Router), TypeScript, Tailwind, Better Auth (JWT); Backend: FastAPI, SQLModel, Python; Database: Neon Serverless PostgreSQL; Auth: Better Auth issues JWT; FastAPI must validate JWT using BETTER_AUTH_SECRET; Spec-Kit + Codex Agents used.
4. Mandatory REST API Endpoints: GET/POST /api/{user_id}/tasks; GET/PUT/DELETE /api/{user_id}/tasks/{id}; PATCH /api/{user_id}/tasks/{id}/complete. All endpoints must require JWT, enforce user isolation, reject unauthorized access.
5. Backend Rules: Must use SQLModel models defined in /specs/database/schema.md; queries filter by authenticated user_id; no endpoint exposes another user’s tasks.
6. Frontend Rules: Must use Better Auth for signup/signin; request JWT; attach JWT to all API calls; UI must follow specs in /specs/ui.
7. Architecture Principles: Monorepo with /frontend, /backend, /specs, /agents; changes must follow the Constitution; API/schema/feature changes updated in specs first.
8. Agent Compliance: Architect, Backend, Frontend, Specs, and DevOps agents must follow this Constitution and may not violate API contract, auth rules, or data ownership.

## Response snapshot

Updated constitution to v2.0.0: mandated full-stack Next.js/FastAPI/Neon/Better Auth stack, specs-first governance, required REST endpoints with JWT isolation, SQLModel enforcement, and agent compliance. Added sync report and kept plan/spec/tasks templates aligned.

## Outcome

- ✅ Impact: Phase II governance codified for full-stack build with strict API/auth/data rules.
- 🧪 Tests: not run (doc-only).
- 📁 Files: .specify/memory/constitution.md updated.
- 🔁 Next prompts: generate Phase II spec/plan/tasks per SpecKit+.
- 🧠 Reflection: Manual PHR creation due to template path constraints; ensure future PHRs run from git root.
