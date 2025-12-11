---
id: 0004
title: phase2-constitution-update
stage: constitution
date: 2025-12-12
surface: specs
model: gpt-5
feature: null
branch: 001-spec-meta-refresh
user: aie
command: manual (constitution update)
labels: [constitution, phase2]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - path: .specify/memory/constitution.md
    note: Updated to v3.0.0 with specs-first priority and Phase II stack/auth mandates.
tests:
  - status: not run
    note: documentation-only change
---

## Prompt

You are Codex, helping build **Phase II** of the Todo App: a full-stack, multi-user web application using a **spec-driven** workflow. 1. **Spec-Driven Development** - Treat everything in `/specs` as the source of truth. - Before implementing anything, read the relevant spec file(s). - If there is a conflict, follow `/specs` first, then the CLAUDE/Constitution files. 2. **Monorepo & Structure** - Root repo: `hackathon-todo/` - Use and respect the Spec-Kit layout: - `.spec-kit/config.yaml` - `specs/overview.md` - `specs/features/*.md` - `specs/api/*.md` - `specs/database/*.md` - `specs/ui/*.md` - Follow guidance in: - `CLAUDE.md` (root) - `frontend/CLAUDE.md` - `backend/CLAUDE.md` 3. **Phase II Scope (Authoritative)** - Objective: Transform the existing console todo app into a **modern multi-user web app** with persistent storage. - All 5 basic Task CRUD features must exist as a **web application**. - Build a **REST API backend** + **Responsive frontend** + **Neon PostgreSQL** + **Better Auth**. 4. **Technology Stack (Mandatory)** - **Frontend** - Next.js 16+ (App Router) - TypeScript - Tailwind CSS - Better Auth for authentication (JWT issuing) - **Backend** - Python - FastAPI - SQLModel (ORM) - Neon Serverless PostgreSQL - **Spec / Tooling** - Codex + GitHub Spec-Kit Plus - **Auth** - Better Auth issues **JWT tokens**. - FastAPI verifies tokens using a **shared secret** (`BETTER_AUTH_SECRET` env var). 5. **REST API Contract (Stable Interface)** The following endpoints are canonical and must be implemented and preserved: - `GET /api/{user_id}/tasks` List all tasks for `user_id`. - `POST /api/{user_id}/tasks` Create a new task for `user_id`. - `GET /api/{user_id}/tasks/{id}` Get task details by task ID (must belong to `user_id`). - `PUT /api/{user_id}/tasks/{id}` Update task (only if owned by `user_id`). - `DELETE /api/{user_id}/tasks/{id}` Delete task (only if owned by `user_id`). - `PATCH /api/{user_id}/tasks/{id}/complete` Toggle completion flag of the task. All endpoints: - Are **JSON-based**. - Must enforce **ownership**: only operate on tasks of the authenticated user. 6. **Authentication & Security Rules** - Every API request must include a **JWT**: - Header: `Authorization: Bearer <token>`. - FastAPI: - Verifies JWT with the shared secret. - Extracts `user_id` from the token. - Cross-checks that `user_id` in URL matches the authenticated user. - If token is missing or invalid: - Respond with `401 Unauthorized`. - If token is valid but the resource does not belong to the user: - Respond with `403 Forbidden` or `404 Not Found` (depending on spec). - Never bypass or stub out auth in production code. 7. **Database & Models** - Use **SQLModel** with Neon PostgreSQL. - Define a `Task` model following `/specs/database/schema.md` and `/specs/features/task-crud.md`. - Every task must be associated with a specific user (by user ID / subject from JWT). - DB connection string comes from `DATABASE_URL` env variable. 8. **Frontend Responsibilities** - Use Better Auth to handle **signup / signin** and session. - Retrieve JWT token and attach it to all backend requests. - Use the REST endpoints above for all task operations. - Implement responsive UI according to `/specs/ui/*.md`. 9. **Code Quality & Conventions** - Match patterns described in the CLAUDE files. - Use small, focused modules and clear naming. - Favor explicit types (TypeScript, Pydantic models, SQLModel models). - Keep API error messages helpful but not overly verbose. 10. **Non-Negotiable Rules** - Do not change the published API route structure without updating `/specs/api/rest-endpoints.md`. - Do not introduce technologies outside the approved stack without being explicitly requested. - Always ensure **user isolation**: users can never see or modify others’ tasks. You must always act in accordance with this Constitution when reading the Plan and Tasks and when generating code or modifications.

## Response snapshot

Updated constitution to v3.0.0: specs-first priority (then CLAUDE/Constitution), Phase II stack and scope, stable REST contract, Better Auth JWT enforcement, monorepo/CLAUDE guidance, and maintained testing/traceability requirements.

## Outcome

- ✅ Impact: Constitution now encodes Phase II rules, stack, auth, and specs-first governance.
- 🧪 Tests: not run (doc-only).
- 📁 Files: .specify/memory/constitution.md updated.
- 🔁 Next prompts: Review templates for priority wording alignment.
- 🧠 Reflection: Ensure future plans/specs cite the new rule order and stable REST contract.

## Evaluation notes (flywheel)

- Failure modes observed: PHR script missing template; created manually.
- Graders run and results (PASS/FAIL): not run
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Restore PHR script template to enable automated PHR creation.
