# Phase II Plan

## Goal
Deliver a full-stack multi-user web application that adheres to the Constitution file and spec-driven development.

## Pillars
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind, Better Auth.
- Backend: FastAPI + SQLModel, Python 3.12+, `uv` for dependencies.
- Database: Neon Serverless PostgreSQL.
- Auth: Better Auth issues JWT; backend validates with `BETTER_AUTH_SECRET`.

## Artifacts
- Specs: `/specs/002-phase2/specify.md`, `/specs/002-phase2/features`, `/specs/002-phase2/api`, `/specs/002-phase2/database`, `/specs/002-phase2/ui`.
- Plan: this file.
- Tasks: `/specs/002-phase2/tasks.md`.

## Phase Flow
1. Research & confirm requirements via specs (Auth + Task CRUD).
2. Design contracts and data models (REST + schema).
3. Implement iteratively with tests (backend + frontend).
4. Validate against specs, coverage, and API contracts.

## Milestones
- M1: Auth flows defined and scaffolded (frontend Better Auth + backend JWT validation stub).
- M2: Task CRUD contracts + schema finalized.
- M3: Backend endpoints implemented with tests and isolation.
- M4: Frontend pages/components wired to API with JWT.
- M5: End-to-end validation and polishing.

## Quality Gates
- Tests: pytest + coverage ≥80% backend; frontend tests as applicable.
- Contracts: API/DB/UI changes must update specs first.
- Security: JWT required on all endpoints; `{user_id}` isolation enforced.

## Traceability
- Constitution file > plan > tasks > specs.
- No code may diverge from specs; specs are updated first by the Specs agent.
