# Phase II Architecture

## Monorepo Layout
- `/frontend`: Next.js 16+ App Router, TypeScript, Tailwind, Better Auth client.
- `/backend`: FastAPI + SQLModel, Python 3.12+, `uv`, JWT validation.
- `/phase2/specs`: feature, API, database, and UI specs (see `/phase2/specify.md`).
- `/agents`: Architect, Backend, Frontend, Specs, DevOps guidance.

## Integration Contracts
- REST endpoints and payloads defined in `/phase2/api/rest-endpoints.md`.
- Schema defined in `/phase2/database/schema.md`.
- UI flows defined in `/phase2/ui`.

## Auth & Isolation
- Better Auth issues JWT; backend validates via `BETTER_AUTH_SECRET`.
- `{user_id}` in path must match authenticated user; enforce isolation on all queries.

## Data Flow
- Frontend → API with JWT header.
- API → Neon PostgreSQL via SQLModel models aligned to schema specs.
