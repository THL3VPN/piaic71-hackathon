# Phase II Meta-Specification

This document explains how Phase II specs are organized under Spec-Kit and how Codex agents must interpret, load, and use them. It defines:
- The purpose of specifications
- How specs relate to the Constitution file, Phase II plan, and tasks
- How multi-agent Codex development should operate
- How phases progress
- Where Phase II specs are stored and how they should be referenced

The `/phase2` specs directory is the authoritative source of truth for Phase II functional and technical behavior. Specifications define **WHAT** the software must do, not HOW it must be implemented. All Codex agents — Architect, Backend, Frontend, Specs, DevOps — must treat `/phase2` specs as the primary reference when generating, modifying, or validating Phase II code. The Constitution file has higher priority than individual specs.

## Spec Structure (Phase II)

```text
/phase2
  specify.md        – This meta-spec (how Phase II specs work)
  plan.md           – Execution strategy for Phase II
  tasks.md          – Actionable checklist for agents
  overview.md       – High-level Phase II overview
  architecture.md   – System architecture description
  /features         – Feature-level functional requirements
  /api              – REST API specifications
  /database         – Schema definitions
  /ui               – UI layout & components
```

Each area has a clear purpose (same mapping as root `/specs` but scoped to Phase II). Specs under `/phase2/features`, `/phase2/api`, `/phase2/database`, and `/phase2/ui` must not contain implementation code.

## Priority Order for Rules (Phase II)

1) Constitution file (global governing rules)  
2) `/phase2/plan.md` (how to implement Phase II)  
3) `/phase2/tasks.md` (what to do, step by step)  
4) Phase II specs:  
   - `/phase2/features/*.md`  
   - `/phase2/api/*.md`  
   - `/phase2/database/*.md`  
   - `/phase2/ui/*.md`  
5) Agent-level instructions under `/agents`  
6) Local folder-level instructions (e.g., `backend/CODEX.md`, `frontend/CODEX.md`)

If a conflict occurs: the Constitution overrides everything. Then `plan.md` overrides `tasks.md`. Specs override any agent-local instruction. Agents must never ignore the Constitution, Plan, or Tasks.

## How Agents Use Phase II Specs
- **Architect**: Ensures structure and tech choices align with Phase II specs and the Constitution; proposes spec changes via Specs Agent.
- **Backend**: Reads feature/API/database specs before coding; follows contracts and schema; treats specs as read-only.
- **Frontend**: Reads feature/UI (and API) specs before coding; follows UI layouts and flows; treats specs as read-only.
- **Specs**: Only agent allowed to modify `/phase2` specs; keeps them accurate and synchronized with behavior.
- **DevOps**: Reads specs to configure infra/tooling; does not modify specs.

## Referencing Phase II Specs

Use Spec-Kit paths, for example:
- `@phase2/features/task-crud.md`
- `@phase2/features/authentication.md`
- `@phase2/api/rest-endpoints.md`
- `@phase2/database/schema.md`
- `@phase2/ui/pages.md`
- `@phase2/ui/components.md`

Before implementing or modifying a feature, endpoint, schema, or UI, agents must first read the relevant Phase II spec file(s).

## Enforcement of Spec-Driven Development

- Code must not contradict Phase II specs.
- If requirements change: Specs Agent updates the relevant Phase II spec(s), then implementation agents adjust code.
- Backend and frontend must:
  - Match REST API definitions exactly (paths, methods, request/response shapes, auth behavior).
  - Use database fields and relations as defined in schema specs.
  - Implement UI behavior as described in UI specs.
- If code and specs diverge: bring code back in line with specs; if specs are outdated, Specs Agent updates them and documents the change.

## JWT, Auth, and API-Level Rules (Phase II)

- All REST API endpoints must follow authentication and user-isolation rules defined in the Constitution and API specs.
- Backend: validate JWT tokens using `BETTER_AUTH_SECRET`; enforce user isolation on all queries.
- Frontend: use Better Auth to acquire JWTs; attach JWTs to all authenticated API requests.
- API specs define required headers, expected status codes, request/response formats.

## Future Extensions

This Phase II meta-spec should support future phases without breaking Phase II behavior. New Phase II specs may be added under `/phase2/features`, `/phase2/api`, `/phase2/database`, or `/phase2/ui`. The Specs Agent ensures compatibility; Constitution and Plan are updated as needed.

## Permissions and Edit Policy

Only the Specs Agent may modify files under `/phase2`, including:
- `specify.md`, `plan.md`, `tasks.md`, `overview.md`, `architecture.md`
- All files under `features/`, `api/`, `database/`, `ui/`

Backend, Frontend, Architect, and DevOps agents must treat `/phase2` specs as read-only. Any change to specs must reflect actual or planned behavior changes, not arbitrary edits.
