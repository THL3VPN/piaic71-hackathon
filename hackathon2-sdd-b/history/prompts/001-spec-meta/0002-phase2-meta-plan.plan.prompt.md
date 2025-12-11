---
id: 0002
title: phase2-meta-plan
stage: plan
date: 2025-12-12
surface: specs
model: gpt-5
feature: 001-spec-meta
branch: 001-spec-meta
user: aie
command: manual (plan generation)
labels: [plan, meta-spec]
links:
  spec: specs/001-spec-meta/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: specs/001-spec-meta/plan.md
    note: Phase II execution plan (no Docker, multi-agent streams).
  - path: specs/001-spec-meta/research.md
    note: Decisions for stack/auth/contract, no clarifications.
  - path: specs/001-spec-meta/data-model.md
    note: Task entity with ownership and validation rules.
  - path: specs/001-spec-meta/contracts/rest-api.md
    note: REST contract summary aligned to API specs.
  - path: specs/001-spec-meta/quickstart.md
    note: Manual dev setup (uvicorn/npm) without Docker.
tests:
  - status: not run
    note: documentation-only change
---

## Prompt

This document defines HOW Phase II of the `hackathon-todo` project will be executed using Spec-Kit and the five Codex agents (Architect, Backend, Frontend, Specs, DevOps). It implements the rules of the Constitution and the structure defined in specify.md. Docker is NOT included in this phase. --- Transform the Phase I console todo application into a multi-user full-stack web application with: - Next.js 16+ (App Router) - Tailwind CSS - Better Auth (JWT issuing) - FastAPI backend - SQLModel ORM - Neon Serverless PostgreSQL - Complete Task CRUD - Enforced user isolation through JWT - Spec-driven multi-agent development This phase provides the full platform for Phase III (chatbot and automation tools). --- Phase II will proceed across five major streams: 1. Backend API development 2. Frontend UI & authentication 3. Database schema + models 4. Authentication via JWT 5. REST API integration Local development will be handled manually (no Docker). --- Responsible for: - Enforcing folder structure and monorepo architecture - Ensuring backend, frontend, and specs follow Constitution rules - Approving structural or architectural changes - Ensuring consistent interpretation of API + auth rules This agent does NOT write backend/frontend code and does NOT modify specs. --- Responsible for implementing: - All REST API endpoints required by `/specs/api/rest-endpoints.md` - SQLModel models based on `/specs/database/schema.md` - JWT validation using the shared secret - User isolation (authenticated user must match user_id in path) - FastAPI application structure, error handling, and response schemas Backend Agent must: - Follow FastAPI + SQLModel conventions - Never violate API spec contract - Never modify specs --- Responsible for: - Next.js 16+ App Router setup - Tailwind CSS configuration - Better Auth integration (JWT issuing) - Login and signup pages - Task dashboard and CRUD UI - Implementing API client that attaches JWT to all requests Frontend Agent must: - Follow UI specs in `/specs/ui` - Follow feature requirements in `/specs/features` - Treat all specs as read-only --- Responsible for: - Maintaining all specification files - Keeping specs aligned with backend and frontend implementation - Updating API, database, UI, and feature specs when requirements change - Maintaining Constitution, Plan, Tasks, and specify.md when needed This is the ONLY agent allowed to modify `/specs`. --- Since Docker is not used in this phase, DevOps responsibilities are: - Managing environment variables (.env.example) - Documenting backend and frontend local setup - Ensuring correct configuration for: - DATABASE_URL - BETTER_AUTH_SECRET - Ensuring backend and frontend can run manually without containerization DevOps Agent must not modify backend or frontend logic. --- The backend must include: - main.py - models.py - schemas.py - db.py - auth.py - routes/tasks.py Architect Agent ensures correct placement and structure. - Implement SQLModel models based on `/specs/database/schema.md` - Connect to Neon PostgreSQL using DATABASE_URL (manual local config) - Include indexing on `user_id` - Implement session dependency in `db.py` - Read JWT from Authorization header - Validate using BETTER_AUTH_SECRET - Extract user_id claim - Enforce user_id match between JWT and path parameter - Reject unauthorized or mismatched access Backend must implement endpoints in `/specs/api/rest-endpoints.md`: - GET /api/{user_id}/tasks - POST /api/{user_id}/tasks - GET /api/{user_id}/tasks/{id} - PUT /api/{user_id}/tasks/{id} - DELETE /api/{user_id}/tasks/{id} - PATCH /api/{user_id}/tasks/{id}/complete Each endpoint must: - Use Pydantic schemas - Enforce user ownership - Return proper status codes - Match API spec contract exactly --- - Initialize Next.js App Router project - Configure TypeScript - Configure Tailwind CSS - Add Better Auth (with JWT issuing enabled) - Set up local environment variables - Build login and signup pages - Handle JWT issuance - Store session securely - Redirect user after login - Create `/tasks` page as the main dashboard - Load tasks from backend - Display list, status, timestamps - Enable creation, editing, deletion of tasks - Implement toggle completion Create `/frontend/lib/api.ts`: - Attach `Authorization: Bearer <token>` - Include authenticated user_id - Implement CRUD methods matching API specs Implement components defined in `/specs/ui`: - TaskList - TaskItem - TaskForm - Filters/sorting (if defined in spec) --- 1. Use SQLModel models defined in `/specs/database/schema.md`. 2. Connect to Neon PostgreSQL manually using DATABASE_URL. 3. Keep schema aligned with specs. 4. Use a simple migration or initial schema creation strategy. 5. Enforce user isolation at the query level:WHERE user_id = authenticated_user_id --- - Better Auth issues JWT - JWT included in all API requests - user_id extracted from session - Validate JWT - Extract and enforce user_id - Return correct error codes on failure --- Since Docker is not used: - Runs manually using `npm run dev` - Must point to backend URL (http://localhost:8000) - Runs via `uvicorn main:app --reload --port 8000` - Must use DATABASE_URL from environment - DATABASE_URL - BETTER_AUTH_SECRET - Start backend - Start frontend - Ensure both use compatible URLs - Confirm JWT roundtrip works --- - JWT validation - User isolation - CRUD operations - Error handling - Login/signup flows - Task listing - Task manipulation UI - Error display - Login → receive JWT → CRUD → logout - User A cannot view/modify User B tasks --- | Agent | Responsibilities | Forbidden | |-------|------------------|----------| | Architect | Structure & consistency | Implement code | | Backend | API, DB, JWT | Edit specs | | Frontend | UI, auth, API client | Edit specs | | Specs | Maintain all specs | Touch code | | DevOps | Env vars & setup docs | Implement logic | All agents must follow the Constitution, Plan, Tasks, and Specs. --- End of plan.md.

## Response snapshot

Generated Phase II plan and design artifacts for the meta-spec: filled plan.md (streams, constitution check, constraints, no Docker), authored research.md (decisions), data-model.md (Task), contracts/rest-api.md (canonical endpoints/auth), and quickstart.md (manual setup). Agent context update attempted; failed due to missing agent-file template upstream.

## Outcome

- ✅ Impact: Plan and Phase 0/1 artifacts ready for Phase II guidance; manual dev workflow documented.
- 🧪 Tests: not run (docs-only).
- 📁 Files: plan.md, research.md, data-model.md, contracts/rest-api.md, quickstart.md added.
- 🔁 Next prompts: Optionally resolve agent-context template gap; proceed to tasks/planning.
- 🧠 Reflection: Maintain specs-first rule and no-Docker constraint in downstream tasks.

## Evaluation notes (flywheel)

- Failure modes observed: update-agent-context script missing template at repo root; noted for follow-up.
- Graders run and results (PASS/FAIL): not run
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Restore agent-file-template to enable context update automation.
