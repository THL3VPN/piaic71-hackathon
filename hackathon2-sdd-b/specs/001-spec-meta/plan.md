# Implementation Plan: Phase II Execution (Spec-Kit Meta)

**Branch**: `001-spec-meta` | **Date**: 2025-12-12 | **Spec**: specs/001-spec-meta/spec.md  
**Input**: Meta-spec for how Phase II specs are organized and applied (`specs/001-spec-meta/spec.md`)

**Note**: Executes the Constitution v3.0.0 and the Phase II meta-spec; Docker is excluded for this phase.

## Summary

Deliver the governance and structure for Phase II as a spec-driven, multi-agent full-stack build (Next.js 16+ with Tailwind and Better Auth; FastAPI + SQLModel on Neon PostgreSQL). Enforce rule priority (Constitution → plan → tasks → specs → agent/local), single Specs Agent ownership of `/specs`, stable REST contract, JWT-based user isolation, and manual local setup (no Docker).

## Technical Context

**Language/Version**: Backend: Python 3.12+; Frontend: TypeScript  
**Primary Dependencies**: FastAPI, SQLModel, Better Auth (JWT), Next.js 16+ (App Router), Tailwind CSS, Neon PostgreSQL  
**Storage**: Neon Serverless PostgreSQL via `DATABASE_URL`  
**Testing**: Backend `uv run pytest --cov`; Frontend `npm test`/`npm run lint`; optional E2E for auth + CRUD  
**Target Platform**: Full-stack web (manual local dev; no Docker)  
**Project Type**: Monorepo with `/backend` and `/frontend` plus `/specs` (Spec-Kit)  
**Performance Goals**: Responsive CRUD UI; API p95 sub-300ms under modest load; dashboard initial load <2.5s  
**Constraints**: No Docker; JWT required on all requests; `{user_id}` must match token; follow `/specs` as source of truth  
**Scale/Scope**: Multi-user task app with per-user isolation; Phase II enables Phase III extensions

## Constitution Check

- Rule priority: `/specs` first, then Codex/Constitution guidance; plans/tasks must cite governing specs.  
- Phase flow: Research → Specification → Design & Contracts → Implementation → Validation; each with artifacts (research.md, spec.md, data-model.md, contracts/, quickstart.md, tasks.md, PHRs).  
- Stack: Next.js 16+/Tailwind/Better Auth; FastAPI + SQLModel + Neon PostgreSQL; JWT auth required.  
- REST contract: `/api/{user_id}/tasks` CRUD + PATCH complete; JSON-only; ownership enforced.  
- Testing: tests before/with implementation; ≥80% coverage on new/changed backend code; frontend tests/lint; record results.  
- No Docker in Phase II; manual local setup documented.  
- Specs-only edits by Specs Agent; implementation agents treat `/specs` as read-only.

## Project Structure

### Documentation (this feature)

```text
specs/001-spec-meta/
├── plan.md           # This file
├── research.md       # Phase 0
├── data-model.md     # Phase 1
├── contracts/        # Phase 1 REST contracts
├── quickstart.md     # Phase 1 setup (manual, no Docker)
└── spec.md           # Meta-spec (source)
```

### Source Code (monorepo)

```text
backend/
├── main.py
├── db.py
├── auth.py
├── models.py
├── schemas.py
└── routes/
    └── tasks.py

frontend/
├── app/
│   ├── login/
│   ├── signup/
│   └── tasks/
├── lib/
│   └── api.ts
├── components/
└── styles/
```

**Structure Decision**: Monorepo with `/backend` (FastAPI + SQLModel) and `/frontend` (Next.js App Router + Better Auth), governed by `/specs` with Specs Agent ownership.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| None | n/a | n/a |

## Execution Streams (Phase II)

1) **Backend API development** — Implement REST endpoints from `/specs/api/rest-endpoints.md`, SQLModel models per `/specs/database/schema.md`, JWT validation, and isolation.  
2) **Frontend UI & authentication** — Next.js App Router with Tailwind and Better Auth; login/signup/tasks pages; `/frontend/lib/api.ts` attaching JWT.  
3) **Database schema + models** — Align SQLModel to schema spec; Neon `DATABASE_URL`; index on `user_id`; simple migration/creation.  
4) **Authentication via JWT** — Better Auth issues JWT; FastAPI validates with `BETTER_AUTH_SECRET`; enforce `{user_id}` parity.  
5) **REST API integration** — Manual local dev (no Docker); frontend calls backend at `http://localhost:8000`; contracts enforced end-to-end.

## Phase 0: Research

- Clarifications: None (requirements explicit: stack, no Docker, rule priority, endpoints, JWT/isolation).  
- Research tasks: best practices for FastAPI + SQLModel with JWT and Neon; Better Auth integration with Next.js App Router; manual local setup without Docker.

## Phase 1: Design & Contracts

- **data-model.md**: Define Task entity per `/specs/database/schema.md` with ownership, timestamps, and validation.  
- **contracts/**: REST contract summary derived from `/specs/api/rest-endpoints.md`; include methods, paths, auth, ownership, status codes, and schemas.  
- **quickstart.md**: Manual setup (no Docker): env vars (`DATABASE_URL`, `BETTER_AUTH_SECRET`), backend `uv run uvicorn backend.main:app --reload --port 8000`, frontend `npm install && npm run dev` pointing to backend.  
- **Agent context**: Run `.specify/scripts/bash/update-agent-context.sh codex` to record new stack context (note: template missing upstream; capture result if it fails).

## Post-Design Constitution Recheck

- Ensure plan/design artifacts align with Constitution v3.0.0: specs-first rule priority, stack mandates, REST contract, JWT/isolation, and testing discipline.

## Acceptance Gates

- Research.md complete with resolved clarifications.  
- Data-model.md, contracts/, quickstart.md generated and aligned to spec.  
- Agent context update attempted; note any template issues.  
- No Docker usage; manual dev workflow documented.  
- REST endpoints and auth/isolation captured in contracts.

## Out of Scope

- Docker/containerization.  
- Phase III chatbot/tooling (future).  
- Non-task features beyond Task CRUD and auth for Phase II.
