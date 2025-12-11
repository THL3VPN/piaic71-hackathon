# Phase II Plan

## Goal
Deliver a full-stack multi-user web application that adheres to the Constitution file and spec-driven development.

## Pillars
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind, Better Auth.
- Backend: FastAPI + SQLModel, Python 3.12+, `uv` for dependencies.
- Database: Neon Serverless PostgreSQL.
- Auth: Better Auth issues JWT; backend validates with `BETTER_AUTH_SECRET`.

## Artifacts
- Specs: `/phase2/specify.md`, `/phase2/features`, `/phase2/api`, `/phase2/database`, `/phase2/ui`.
- Plan: this file.
- Tasks: `/phase2/tasks.md`.

## Phase Flow
1. Research & confirm requirements via specs.
2. Design contracts and data models.
3. Implement iteratively with tests.
4. Validate against specs, coverage, and API contracts.

## Traceability
- Constitution file > plan > tasks > specs.
- No code may diverge from specs; specs are updated first by the Specs agent.
