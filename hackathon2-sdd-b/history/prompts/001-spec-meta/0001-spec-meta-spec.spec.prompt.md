---
id: 0001
title: spec-meta-spec
stage: spec
date: 2025-12-12
surface: specs
model: gpt-5
feature: 001-spec-meta
branch: 001-spec-meta
user: aie
command: manual (spec generation)
labels: [spec, meta-spec]
links:
  spec: specs/001-spec-meta/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: specs/001-spec-meta/spec.md
    note: Drafted meta-spec defining specs structure, rule priority, agent roles, and Phase II enforcement.
  - path: specs/001-spec-meta/checklists/requirements.md
    note: Checklist validated; all items marked complete.
tests:
  - status: not run
    note: documentation-only change
---

## Prompt

This document explains how the `hackathon-todo` project is organized under Spec-Kit and how Codex agents must interpret, load, and apply the specifications. It defines: - The purpose of specifications - How specs relate to the Constitution, Plan, and Tasks - How multi-agent Codex development works - How phases progress - The structure of the /specs directory - The rules and priorities agents must follow --- The `/specs` directory is the authoritative source of truth for the entire project. Specifications define WHAT the system must do, not HOW it is implemented. All Codex agents — Architect, Backend, Frontend, Specs, and DevOps — must treat `/specs` as the primary reference for correctness and project alignment. A separate **Constitution** defines global governing rules and has the highest priority. --- The specification files must follow this structure: /specs specify.md – This meta-spec (how specs work) plan.md – Execution plan for the current phase tasks.md – Actionable task list for Codex agents overview.md – High-level overview of the project architecture.md – Architecture description /features – Feature-level functional requirements /api – REST API specifications /database – Data model and schema definitions /ui – UI layout and component descriptions Each category has a distinct purpose: - specify.md: Rules for how specs & agents interact - plan.md: Strategy for implementing the current phase - tasks.md: Ordered checklist for development - overview.md: Project vision & context - architecture.md: System-level design decisions - features/: User stories & functional behavior - api/: Endpoint contracts - database/: Schema definitions - ui/: Page flows & components Specs must NOT contain implementation code. --- - Phase I: Console application (completed) - Phase II: Full-stack web application (current) Codex agents must always operate according to the currently active phase. Feature specifications are mapped to phases in `.spec-kit/config.yaml`. --- Codex agents must follow rules in this exact order: 1. The Constitution (global governing rules) 2. plan.md 3. tasks.md 4. Specifications under: - /specs/features - /specs/api - /specs/database - /specs/ui 5. Agent instruction files under /agents 6. Local folder CODEX.md files (backend/, frontend/) Conflict resolution: - The Constitution overrides everything. - plan.md overrides tasks.md. - Specs override any agent-local instructions. - Backend/Frontend logic may never contradict specs. --- - Ensures structure, folder conventions, and architecture match the Constitution and specs. - Guides alignment but does NOT write backend/frontend logic. - May request specs updates but must not edit them directly. - Reads feature, API, and database specs. - Implements FastAPI backend, SQLModel models, JWT auth, and REST logic. - Must follow API contracts exactly. - Cannot modify any spec file. - Reads UI + feature specs (and API specs when needed). - Implements Next.js UI, Better Auth integration, and API client. - Must not change specs. - The ONLY agent allowed to modify specification files. - Updates specs when behavior or requirements evolve. - Ensures specs remain the source of truth. - Reads specs for environment, infra, and service requirements. - Builds docker-compose, env files, and related tooling. - Does NOT modify specs. --- Codex agents must reference specs using Spec-Kit paths: @specs/features/task-crud.md @specs/features/authentication.md @specs/api/rest-endpoints.md @specs/database/schema.md @specs/ui/pages.md @specs/ui/components.md Agents must read relevant specs BEFORE generating or modifying code. --- To maintain correctness: - Code may not contradict specifications. - If requirements change: - Specs Agent updates the spec - Backend/Frontend Agents adjust implementation - API behavior must match the REST API specifications exactly: - URLs - Methods - Headers - Response shapes - Status codes - Database models must match schema specifications. - UI must match UI flow & component specs. Divergence rules: - Prefer modifying code to match existing specs. - Modify specs only when the actual requirement changes (Specs Agent only). --- Phase II requires: - JWT authentication for all API endpoints. - Backend must validate JWT with the shared secret. - Frontend must attach JWT on every API call. - User isolation must be enforced (each user sees only their data). API specs under `/specs/api` define: - Required headers - Request/response contracts - Expected status codes - Security rules Agents must implement behavior strictly according to these specifications. --- This meta-spec supports future extensions: - Chatbot agent integration - MCP tools - More API endpoints - Additional UI components When new features are added: - Specs are expanded - Constitution/Plan updated where required - Implementation agents follow updated specs ---

## Response snapshot

Generated the Phase II meta-spec for Spec-Kit: defined `/specs` as source of truth, structure/purpose of each file, rule priority (Constitution → plan → tasks → specs → agent/local), agent roles and edit policy (Specs Agent only editor), Phase II mandates (stable REST, JWT, user isolation), and future extension guidance. Added checklist with all items passing.

## Outcome

- ✅ Impact: Meta-spec now directs all agents on rule order, structure, permissions, and Phase II security/contract requirements.
- 🧪 Tests: not run (doc-only).
- 📁 Files: specs/001-spec-meta/spec.md drafted; checklist added.
- 🔁 Next prompts: None required before planning; proceed to `/sp.plan` when ready.
- 🧠 Reflection: Keep rule-priority wording aligned in templates and downstream plans/tasks.

## Evaluation notes (flywheel)

- Failure modes observed: PHR script template missing; created PHR manually.
- Graders run and results (PASS/FAIL): not run
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Restore PHR script template to automate future PHR creation.
