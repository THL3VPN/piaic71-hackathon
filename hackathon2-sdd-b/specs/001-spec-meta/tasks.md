# Tasks: Phase II Execution (Spec-Kit Meta)

**Feature**: specs/001-spec-meta/spec.md  
**Plan**: specs/001-spec-meta/plan.md  
**Scope**: Phase II full-stack web app (manual local dev, no Docker).  
**Rule Priority**: Constitution → plan → tasks → specs → agent/local.

## Phase 1 – Setup

- [ ] T001 Document local env variables in .env.example for backend/frontend (`DATABASE_URL`, `BETTER_AUTH_SECRET`) in specs/001-spec-meta/quickstart.md
- [X] T002 Confirm backend scaffold paths exist or are planned (backend/main.py, db.py, auth.py, models.py, schemas.py, routes/tasks.py) per specs/001-spec-meta/plan.md
- [X] T003 Confirm frontend scaffold paths exist or are planned (frontend/app/login, frontend/app/signup, frontend/app/tasks, frontend/lib/api.ts, frontend/components) per specs/001-spec-meta/plan.md

## Phase 2 – Foundational

- [X] T004 Create/update env setup guide (manual, no Docker) in specs/001-spec-meta/quickstart.md referencing http://localhost:8000 for API
- [X] T005 Add ownership/indexing note for `user_id` to backend/db.py setup guidance in specs/001-spec-meta/plan.md
- [X] T006 Record Neon connection and JWT secret handling steps in specs/001-spec-meta/research.md

## Phase 3 – User Story 1 (P1) Auth & Isolation

**Goal**: Enforce JWT auth and `{user_id}` ownership across backend.

- [X] T007 [US1] Define auth dependency to verify JWT with `BETTER_AUTH_SECRET` in backend/auth.py
- [X] T008 [US1] Wire auth dependency into FastAPI app startup in backend/main.py
- [X] T009 [P] [US1] Enforce `{user_id}` path/user match in backend/routes/tasks.py for all routes
- [X] T010 [P] [US1] Add DB session dependency with user scoping helper in backend/db.py
- [X] T011 [US1] Update response/error handling for 401/403/404 per specs/api/rest-endpoints.md in backend/routes/tasks.py

## Phase 4 – User Story 2 (P2) Task CRUD API

**Goal**: Implement Task CRUD endpoints per REST contract with SQLModel.

- [X] T012 [US2] Define Task model (SQLModel) per specs/001-spec-meta/data-model.md in backend/models.py
- [X] T013 [P] [US2] Create Pydantic schemas for request/response in backend/schemas.py
- [X] T014 [P] [US2] Implement GET/POST /api/{user_id}/tasks handlers in backend/routes/tasks.py
- [X] T015 [P] [US2] Implement GET/PUT/DELETE /api/{user_id}/tasks/{id} in backend/routes/tasks.py
- [X] T016 [P] [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete (idempotent) in backend/routes/tasks.py
- [X] T017 [US2] Align validation (title 1..200, description ≤2000) and status codes with contracts in backend/routes/tasks.py

## Phase 5 – User Story 3 (P3) Frontend Auth + Tasks UI

**Goal**: Next.js App Router UI with Better Auth and task CRUD.

- [X] T018 [US3] Configure Better Auth and JWT storage in frontend/app/login and frontend/app/signup flows
- [X] T019 [P] [US3] Build `/frontend/lib/api.ts` to attach `Authorization: Bearer <token>` and include authenticated user_id
- [X] T020 [P] [US3] Implement tasks dashboard page at frontend/app/tasks/page.tsx with list, status, timestamps
- [X] T021 [P] [US3] Create task form component (create/update) in frontend/components/TaskForm.tsx
- [X] T022 [P] [US3] Create task list/item components with toggle/delete actions in frontend/components/TaskList.tsx and TaskItem.tsx
- [X] T023 [US3] Wire CRUD calls (load/create/update/delete/toggle) to backend endpoints in frontend/app/tasks/page.tsx

## Final Phase – Polish & Cross-Cutting

- [X] T024 Add manual E2E sanity steps (login → CRUD → logout) to specs/001-spec-meta/quickstart.md
- [X] T025 Document rule priority and agent edit policy summary in specs/001-spec-meta/spec.md
- [X] T026 Validate alignment to Constitution v3.0.0 (REST contract, JWT, no Docker) in specs/001-spec-meta/plan.md

## Dependencies (Story Order)

US1 (Auth & Isolation) → US2 (Task CRUD API) → US3 (Frontend Auth + UI)

## Parallel Execution Examples

- US1: T009/T010 can proceed in parallel after T007/T008.  
- US2: T013/T014/T015/T016 can proceed in parallel after T012.  
- US3: T019/T020/T021/T022 can proceed in parallel after T018.

## Implementation Strategy

- MVP: Complete US1 (auth + isolation) and baseline Task CRUD API (T012–T016) to unblock frontend.  
- Incremental delivery: land backend auth/CRUD first, then frontend auth flows, then dashboard CRUD wiring.  
- Always align code to specs and REST contracts; update specs only via Specs Agent if requirements change.
