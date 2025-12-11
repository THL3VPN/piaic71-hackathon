# Phase II Plan – Full-Stack Web Application

This plan defines **how** the project will be executed in Phase II using Spec-Kit and the 5-agent Codex architecture (Architect, Backend, Frontend, Specs, DevOps).  
It translates high-level goals from the Constitution into an actionable development strategy.

---

## 1. Phase II Objective

Transform the Phase I console todo application into a **modern, multi-user full-stack web application** with:

- Next.js 16+ frontend  
- FastAPI backend  
- SQLModel ORM  
- Neon Serverless PostgreSQL database  
- Better Auth authentication with JWT  
- Complete Task CRUD with user isolation  
- Spec-driven multi-agent implementation  

This phase establishes the full platform required for Phase III (chatbot and tool automation).

---

## 2. High-Level Implementation Roadmap

The project will be executed in six major streams:

1. **Backend Implementation (FastAPI + SQLModel)**
2. **Frontend Implementation (Next.js + Better Auth)**
3. **Database Schema Integration (Neon PostgreSQL)**
4. **Authentication via JWT (Better Auth → FastAPI)**
5. **REST API contract execution**
6. **Infrastructure + tooling (DevOps agent)**

All steps follow:

1. Constitution  
2. This Plan  
3. Tasks  
4. Specs  

---

## 3. Multi-Agent Execution Strategy

### 3.1 Architect Agent
Responsible for:

- Monorepo structure validation  
- Backend/frontend folder layout  
- Enforcing architecture consistency  
- Reviewing and approving cross-cutting changes  
- Ensuring all agents follow Constitution + specify.md  

Architect Agent does NOT implement backend/frontend code.  
It ensures **alignment**, not **execution**.

---

### 3.2 Backend Agent
Responsible for implementing:

- `/api/{user_id}/tasks` REST endpoints  
- SQLModel models  
- Database engine + session management  
- JWT verification middleware  
- User isolation enforcement  
- Data validation and error handling  

Backend Agent must:

- Read all API, feature, and database specs  
- Follow FastAPI conventions  
- Never modify specs directly  
- Match API contract **exactly**  

---

### 3.3 Frontend Agent
Responsible for:

- Next.js 16+ App Router setup  
- Better Auth integration (JWT issuing)  
- Login & signup pages  
- Tasks dashboard  
- Task CRUD UI  
- `/frontend/lib/api.ts` client that attaches JWT  

Frontend Agent must:

- Always attach JWT to backend requests  
- Follow UI specs (pages + components)  
- Follow feature specs  
- Treat specs as read-only  

---

### 3.4 Specs Agent
Responsible for maintaining ALL `/specs` files:

- Feature specs  
- API endpoint definitions  
- DB schema  
- UI specs  
- Constitution, Plan, Tasks, specify.md (if needed)  

Specs Agent is the ONLY agent allowed to update specs.  
Specs must remain synchronized with backend and frontend behavior.

---

### 3.5 DevOps Agent
Responsible for:

- docker-compose.yml for full stack  
- Environment variable structure  
- .env.example  
- Neon DB connection handling  
- Local dev workflow documentation  

DevOps Agent must not implement backend/frontend logic.

---

## 4. Backend Implementation Plan (FastAPI)

1. Create backend folder structure:
   - `main.py`
   - `models.py`
   - `schemas.py`
   - `db.py`
   - `auth.py`
   - `routes/tasks.py`

2. Implement SQLModel `Task` model based on:
   - `specs/002-phase2/database/schema.md`

3. Establish Neon PostgreSQL connection (`DATABASE_URL`).

4. Implement JWT verification using shared secret (`BETTER_AUTH_SECRET`).

5. Enforce user isolation:
   - Decode JWT → extract user_id  
   - Compare path user_id → JWT user_id  
   - Reject mismatches  

6. Implement REST API endpoints:
   - GET: List tasks
   - POST: Create task
   - GET: Retrieve single task
   - PUT: Update task
   - DELETE: Delete task
   - PATCH: Toggle completion

7. Ensure all endpoints:
   - Validate input with Pydantic schemas  
   - Return correct JSON shapes  
   - Follow API spec contract  
   - Respond with correct status codes  

---

## 5. Frontend Implementation Plan (Next.js + Better Auth)

1. Initialize Next.js App Router project inside `/frontend`.

2. Configure:
   - TypeScript
   - Tailwind CSS
   - Better Auth (JWT enabled)
   - Environment variables

3. Create pages:
   - `/login`
   - `/signup`
   - `/tasks` (dashboard)
   - Components for task list, task form, filters

4. Implement API client:
   - Stored in `/frontend/lib/api.ts`
   - Automatically attaches JWT in `Authorization: Bearer <token>`
   - Uses authenticated user_id

5. UI behavior:
   - Fetch tasks on page load
   - Optimistic updates or revalidation
   - Responsive Tailwind components

---

## 6. Database Integration Plan

1. Define schema in:
   - `/specs/002-phase2/database/schema.md`

2. Implement SQLModel models accordingly.

3. Connect FastAPI → Neon using:
   - Connection pooling  
   - Async or sync engine (project-dependent)

4. Auto-migrate or manual migration strategy (simple for Phase II).

5. Ensure:
   - Index on user_id  
   - Correct timestamp fields  
   - Ownership enforced at query level  

---

## 7. Authentication Plan (Better Auth → FASTAPI via JWT)

### Frontend responsibilities:
- Login → Better Auth issues JWT  
- Store JWT securely  
- Send token with API requests  

### Backend responsibilities:
- Verify JWT using shared secret  
- Extract user_id claim  
- Compare user_id with URL parameter  

Rules:
- No endpoint should return or accept data from another user  
- Unauthenticated → 401  
- Unauthorized → 403 or 404 (per spec)  

---

## 8. Integration Plan

1. Use docker-compose to orchestrate:
   - Backend service (FastAPI)  
   - Frontend service (Next.js)  
   - Neon PostgreSQL (via external connection)  

2. Shared environment:
   - `DATABASE_URL`
   - `BETTER_AUTH_SECRET`

3. Ensure frontend calls backend via internal network (`http://backend:8000`).

4. CORS only applied if needed.

---

## 9. Testing & Validation Plan

### Backend:
- Test JWT enforcement  
- Test user isolation  
- Test CRUD operations  
- Test invalid data responses  

### Frontend:
- Test login/signup  
- Test task creation and editing  
- Test API error display  
- Test responsive layout  

### Integration:
- End-to-end login → CRUD → logout success path  

---

## 10. Multi-Agent Workflow Summary

| Agent | Primary Workload | Restrictions |
|-------|------------------|-------------|
| **Architect Agent** | Structure, architecture, consistency | No code implementation |
| **Backend Agent** | API, DB, JWT, CRUD logic | Cannot modify specs |
| **Frontend Agent** | UI, API consumption, Better Auth | Cannot modify specs |
| **Specs Agent** | Maintains all specs | Cannot touch code |
| **DevOps Agent** | docker, env, tooling | Cannot implement logic |

Agents must collaborate but operate within boundaries.
