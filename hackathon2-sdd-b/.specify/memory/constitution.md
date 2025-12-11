<!--
Sync Impact Report
- Version: 2.0.0 → 3.0.0
- Modified principles: Spec-Driven Full-Stack Delivery → Spec-Driven Rule Priority & Governance; Python 3.12 + uv Reproducibility → Phase II Stack & Monorepo; API & Data Ownership Enforcement → Auth & Ownership Enforcement
- Added sections: Stable REST Contract; Monorepo Structure & agent guidance; Better Auth & JWT enforcement
- Removed sections: uv-only mandate (replaced by stack mandate), CLI-only references
- Templates requiring updates: .specify/templates/plan-template.md ⚠ review rule priority wording; .specify/templates/spec-template.md ⚠ ensure specs-first language; .specify/templates/tasks-template.md ⚠ align phase references; .specify/templates/commands/*.md ⚠ check for outdated priority/order mentions
- Follow-up TODOs: None identified
-->
# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Rule Priority & Governance (NON-NEGOTIABLE)
`/specs` is the source of truth for functional and technical behavior. Agents must read relevant specs before any implementation. When instructions conflict, follow `/specs` first, then Codex/Constitution guidance. Specs must be authored and updated via Spec-Kit. No work may bypass or contradict specs.

### II. Full-Stack Phase II Scope & Stack
Phase II builds a modern multi-user web app with persistent storage: frontend (Next.js 16+ App Router, TypeScript, Tailwind, Better Auth), backend (FastAPI + SQLModel), Neon PostgreSQL database, spec-driven development, and Better Auth-issued JWTs. All five Task CRUD operations must be delivered as a web application.

### III. Stable REST Contract
The REST API contract is canonical and must be preserved: `GET/POST /api/{user_id}/tasks`, `GET/PUT/DELETE /api/{user_id}/tasks/{id}`, `PATCH /api/{user_id}/tasks/{id}/complete`. All endpoints are JSON, enforce ownership, and follow `/specs/api/rest-endpoints.md`.

### IV. Auth & Ownership Enforcement
Every API request requires `Authorization: Bearer <token>`. FastAPI verifies JWTs with `BETTER_AUTH_SECRET`, extracts `user_id`, and cross-checks the URL `user_id`. Missing/invalid tokens return 401; cross-user access returns 403 or 404 per spec. Never bypass or stub auth in production. All data is isolated per user.

### V. Test Discipline & Coverage
Tests are authored before or alongside implementation. All tests must pass at all times. Coverage must be ≥80% for new/changed code, with explicit rationale for any gaps. Failing tests or coverage regressions block release.

### VI. Monorepo Structure & Agent Guidance
Use and respect the Spec-Kit layout in `hackathon-todo/`: `.spec-kit/config.yaml`, `specs/overview.md`, `specs/features/*.md`, `specs/api/*.md`, `specs/database/*.md`, `specs/ui/*.md`, plus agent guidance files (e.g., `AGENTS.md`, backend/frontend instructions). Agents must align folder structure and work products with these references.

### VII. Reviewable & Traceable Work
Plans, specs, tasks, and code changes must reference each other for traceability. Every change must have clear acceptance criteria, test evidence, coverage data, and a Prompt History Record (PHR) captured before merge. Specs are updated first; implementation follows.

## Technical Constraints & Quality Requirements
- Frontend: Next.js 16+ (App Router), TypeScript, Tailwind, Better Auth for authentication and JWT issuing.
- Backend: FastAPI + SQLModel on Python with Neon PostgreSQL via `DATABASE_URL`.
- Auth: Better Auth issues JWT; FastAPI validates JWT using `BETTER_AUTH_SECRET`; every request must carry `Authorization: Bearer <token>`.
- REST contract: Endpoints listed in Principle III are stable and must remain JSON-only with ownership enforcement.
- Data model: `Task` follows `/specs/database/schema.md` and `/specs/features/task-crud.md`; every task is tied to the authenticated `user_id`.
- Error handling: Helpful, concise API errors; avoid stubbing or bypassing auth.
- Code quality: Small, focused modules with explicit types; follow Codex/agent guidance in root, frontend, and backend.
- Tooling: Use Spec-Kit and GitHub workflows; do not introduce unapproved technologies without explicit request.

## Development Workflow & Phases
1. **Research**: Capture context, risks, and success measures.  
2. **Specification**: Write clear, testable specs informed by research; `/specs` is authoritative.  
3. **Design & Contracts**: Define data models, contracts, and plan structure aligned to specs; exit requires review.  
4. **Implementation**: Build to spec with tests-first; keep changes scoped to planned increments.  
5. **Validation & Release**: Run tests with coverage, document results, and capture user-facing validation before release.

Phase transitions require explicit acceptance of the prior phase artifact. Work too large for a phase must be split before Implementation.

## Governance
- Rule priority: `/specs` prevails, then Codex/Constitution guidance. Tasks and plans must cite the governing spec sections.  
- Amendments require a proposal, impact analysis, semantic version bump (MAJOR for rule redefinition/removal, MINOR for new/expanded guidance, PATCH for clarifications), and reviewer approval.  
- Compliance checks: every PR states phase, artifacts produced, test results, coverage numbers, and links to the relevant PHR. Deviations require time-bound remediation tasks.  
- Runtime guidance (e.g., quickstart or agent guides) must stay in sync with this constitution and `/specs`.  
- Agents (Architect, Backend, Frontend, Specs, DevOps) must enforce this constitution, REST contract, auth rules, and user isolation.

**Version**: 3.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-12
