# Phase II Tasks – 002-phase2

## Phase 1 – Setup
- [ ] T001 Validate monorepo structure (/backend, /frontend, /specs, /agents) against Constitution
- [ ] T002 Create backend skeleton files: backend/main.py, backend/models.py, backend/schemas.py, backend/db.py, backend/auth.py, backend/routes/tasks.py
- [ ] T003 Create frontend skeleton (Next.js App Router): frontend/app/, frontend/lib/api.ts, frontend/components/, frontend/styles/
- [ ] T004 Create .env.example with DATABASE_URL and BETTER_AUTH_SECRET

## Phase 2 – Foundational (blocking)
- [ ] T005 Implement SQLModel engine/session in backend/db.py using DATABASE_URL (Neon)
- [ ] T006 Define Task model in backend/models.py per specs/002-phase2/database/schema.md (fields + index on user_id)
- [ ] T007 Add Pydantic schemas in backend/schemas.py (create/update/read with validation: title 1..200, description ≤2000)
- [ ] T008 Configure FastAPI app in backend/main.py with routes/tasks.py mounted
- [ ] T009 Configure CORS in backend/main.py only if frontend origin requires it
- [ ] T010 Implement JWT verification helper in backend/auth.py (BETTER_AUTH_SECRET, extract user_id, 401 on invalid/missing)
- [ ] T011 Enforce path user_id vs JWT user_id check (403/404 per spec) in route dependencies
- [ ] T012 Update specs alignment (Specs agent): ensure specs/002-phase2/api/rest-endpoints.md matches planned responses/status codes

## Phase 3 – User Story 1: Authentication (P1)
- [ ] T013 [US1] Integrate Better Auth client in frontend (config, env wiring)
- [ ] T014 [US1] Implement signup page frontend/app/signup/page.tsx with Better Auth flow
- [ ] T015 [US1] Implement login page frontend/app/login/page.tsx with Better Auth flow
- [ ] T016 [US1] Store JWT via Better Auth session and expose accessor in frontend/lib/api.ts
- [ ] T017 [US1] Backend: ensure JWT middleware applied to all task routes (backend/auth.py, backend/routes/tasks.py)
- [ ] T018 [US1] Specs agent: update specs/002-phase2/features/authentication.md if behaviors change during integration

## Phase 4 – User Story 2: Task CRUD (P1)
- [ ] T019 [US2] Implement GET /api/{user_id}/tasks in backend/routes/tasks.py with filters (status, limit/offset, sort)
- [ ] T020 [US2] Implement POST /api/{user_id}/tasks in backend/routes/tasks.py (validate payload, set completed=false)
- [ ] T021 [US2] Implement GET /api/{user_id}/tasks/{id} in backend/routes/tasks.py (user isolation)
- [ ] T022 [US2] Implement PUT /api/{user_id}/tasks/{id} in backend/routes/tasks.py (replace fields, validate)
- [ ] T023 [US2] Implement PATCH /api/{user_id}/tasks/{id}/complete in backend/routes/tasks.py (idempotent complete)
- [ ] T024 [US2] Implement DELETE /api/{user_id}/tasks/{id} in backend/routes/tasks.py
- [ ] T025 [US2] Wire frontend/lib/api.ts client functions (getTasks, createTask, updateTask, deleteTask, toggleTaskComplete) attaching JWT
- [ ] T026 [US2] Build TaskList component frontend/components/TaskList.tsx with loading/empty/error states
- [ ] T027 [US2] Build TaskItem component frontend/components/TaskItem.tsx with actions (edit/delete/complete)
- [ ] T028 [US2] Build TaskForm component frontend/components/TaskForm.tsx with validation messages
- [ ] T029 [US2] Build filters/sorting UI frontend/components/Filters.tsx consistent with API params
- [ ] T030 [US2] Implement /tasks dashboard page frontend/app/tasks/page.tsx (fetch on load, revalidate on change)
- [ ] T031 [US2] Specs agent: update specs/002-phase2/features/task-crud.md and specs/002-phase2/api/rest-endpoints.md if behavior changes

## Phase 5 – Validation & Testing
- [ ] T032 Backend tests: pytest for JWT auth, user isolation, CRUD happy/edge paths (backend/tests/)
- [ ] T033 Backend tests: validation errors (title empty/long, description too long) return 400
- [ ] T034 Backend tests: 401 for missing/invalid JWT; 403/404 for cross-user access
- [ ] T035 Frontend tests (if applicable): render TaskList empty/loading/error; api client attaches JWT
- [ ] T036 End-to-end sanity: login → create/edit/complete/delete task → verify isolation
- [ ] T037 Coverage check ≥80% backend; report in PR (per Constitution)

## Dependencies
- Setup (Phase 1) → Foundational (Phase 2) → US1 Auth → US2 Task CRUD → Validation.
- Auth (US1) must precede Task CRUD (US2) for JWT-protected calls.

## Parallelizable Examples
- [P] T003 (frontend skeleton) can run with T002 (backend skeleton).
- [P] T005-T007 (DB model/schemas) can run with T008 (app wiring) after skeletons.
- [P] T025-T029 (frontend components) can run in parallel once API contracts are stable.

## Implementation Strategy
- MVP: complete US1 (Auth) + minimal Task CRUD happy path (list/create) with isolation.
- Iterate to full CRUD, filters, and robust error handling.
- Enforce specs-first: any contract/UI/schema change must be updated by Specs agent before code.
