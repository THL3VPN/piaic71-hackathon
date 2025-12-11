# Phase II Tasks – 002-phase2

## Phase 1 – Setup
- [ ] T001 Validate monorepo structure (/backend, /frontend, /specs, /agents) against Constitution
- [ ] T002 Create backend skeleton files: backend/main.py, backend/models.py, backend/schemas.py, backend/db.py, backend/auth.py, backend/routes/tasks.py
- [ ] T003 Create frontend skeleton (Next.js App Router): frontend/app/, frontend/lib/api.ts, frontend/components/, frontend/styles/
- [ ] T004 Create .env.example with DATABASE_URL and BETTER_AUTH_SECRET
- [ ] T005 Create docker-compose.yml for backend, frontend, Neon connection/proxy
- [ ] T006 Add README sections for backend/frontend/devcontainer/docker-compose usage

## Phase 2 – Foundational (blocking)
- [ ] T007 Implement SQLModel engine/session in backend/db.py using DATABASE_URL (Neon)
- [ ] T008 Define Task model in backend/models.py per specs/002-phase2/database/schema.md (fields + index on user_id)
- [ ] T009 Add Pydantic schemas in backend/schemas.py (create/update/read with validation: title 1..200, description ≤2000)
- [ ] T010 Configure FastAPI app in backend/main.py with routes/tasks.py mounted
- [ ] T011 Configure CORS in backend/main.py only if frontend origin requires it
- [ ] T012 Implement JWT verification helper in backend/auth.py (BETTER_AUTH_SECRET, extract user_id, 401 on invalid/missing)
- [ ] T013 Enforce path user_id vs JWT user_id check (403/404 per spec) in route dependencies
- [ ] T014 Update specs alignment (Specs agent): ensure specs/002-phase2/api/rest-endpoints.md matches planned responses/status codes

## Phase 3 – User Story 1: Authentication (P1)
- [ ] T015 [US1] Integrate Better Auth client in frontend (config, env wiring)
- [ ] T016 [US1] Implement signup page frontend/app/signup/page.tsx with Better Auth flow
- [ ] T017 [US1] Implement login page frontend/app/login/page.tsx with Better Auth flow
- [ ] T018 [US1] Store JWT via Better Auth session and expose accessor in frontend/lib/api.ts
- [ ] T019 [US1] Backend: ensure JWT middleware applied to all task routes (backend/auth.py, backend/routes/tasks.py)
- [ ] T020 [US1] Specs agent: update specs/002-phase2/features/authentication.md if behaviors change during integration

## Phase 4 – User Story 2: Task CRUD (P1)
- [ ] T021 [US2] Implement GET /api/{user_id}/tasks in backend/routes/tasks.py with filters (status, limit/offset, sort)
- [ ] T022 [US2] Implement POST /api/{user_id}/tasks in backend/routes/tasks.py (validate payload, set completed=false)
- [ ] T023 [US2] Implement GET /api/{user_id}/tasks/{id} in backend/routes/tasks.py (user isolation)
- [ ] T024 [US2] Implement PUT /api/{user_id}/tasks/{id} in backend/routes/tasks.py (replace fields, validate)
- [ ] T025 [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete in backend/routes/tasks.py (idempotent complete)
- [ ] T026 [US2] Implement DELETE /api/{user_id}/tasks/{id} in backend/routes/tasks.py
- [ ] T027 [US2] Wire frontend/lib/api.ts client functions (getTasks, createTask, updateTask, deleteTask, toggleTaskComplete) attaching JWT
- [ ] T028 [US2] Build TaskList component frontend/components/TaskList.tsx with loading/empty/error states
- [ ] T029 [US2] Build TaskItem component frontend/components/TaskItem.tsx with actions (edit/delete/complete)
- [ ] T030 [US2] Build TaskForm component frontend/components/TaskForm.tsx with validation messages
- [ ] T031 [US2] Build filters/sorting UI frontend/components/Filters.tsx consistent with API params
- [ ] T032 [US2] Implement /tasks dashboard page frontend/app/tasks/page.tsx (fetch on load, revalidate on change)
- [ ] T033 [US2] Specs agent: update specs/002-phase2/features/task-crud.md and specs/002-phase2/api/rest-endpoints.md if behavior changes

## Phase 5 – DevOps & Environment
- [ ] T034 Add backend service to docker-compose.yml with uvicorn command and env wiring
- [ ] T035 Add frontend service to docker-compose.yml with Next.js dev server and env wiring
- [ ] T036 Document env vars and compose usage in README (run, stop, logs)

## Phase 6 – Validation & Testing
- [ ] T037 Backend tests: pytest for JWT auth, user isolation, CRUD happy/edge paths (backend/tests/)
- [ ] T038 Backend tests: validation errors (title empty/long, description too long) return 400
- [ ] T039 Backend tests: 401 for missing/invalid JWT; 403/404 for cross-user access
- [ ] T040 Frontend tests (if applicable): render TaskList empty/loading/error; api client attaches JWT
- [ ] T041 End-to-end sanity: login → create/edit/complete/delete task → verify isolation
- [ ] T042 Coverage check ≥80% backend; report in PR (per Constitution)

## Dependencies
- Setup (Phase 1) → Foundational (Phase 2) → US1 Auth → US2 Task CRUD → Validation.
- Auth (US1) must precede Task CRUD (US2) for JWT-protected calls.

## Parallelizable Examples
- [P] T003 (frontend skeleton) can run with T002 (backend skeleton).
- [P] T007-T009 (DB model/schemas) can run with T010 (app wiring) after skeletons.
- [P] T027-T031 (frontend components) can run in parallel once API contracts are stable.

## Implementation Strategy
- MVP: complete US1 (Auth) + minimal Task CRUD happy path (list/create) with isolation.
- Iterate to full CRUD, filters, and robust error handling.
- Enforce specs-first: any contract/UI/schema change must be updated by Specs agent before code.
