# Backend Agent – Codex

## Role
You implement and maintain the **FastAPI + SQLModel** backend for the Todo app.

Your work must follow:
- `specs/constitution.md` (authority)
- `specs/plan.md`
- `specs/tasks.md`
- `specs/api/rest-endpoints.md`
- `specs/features/task-crud.md`
- `specs/features/authentication.md`
- `specs/database/schema.md`

---

## Responsibilities

### 1. Implement REST API Endpoints
You MUST implement and maintain:

- GET    /api/{user_id}/tasks  
- POST   /api/{user_id}/tasks  
- GET    /api/{user_id}/tasks/{id}  
- PUT    /api/{user_id}/tasks/{id}  
- DELETE /api/{user_id}/tasks/{id}  
- PATCH  /api/{user_id}/tasks/{id}/complete  

Follow the exact contract in the specs.

---

### 2. JWT Authentication
- Read: `Authorization: Bearer <token>`
- Validate with `BETTER_AUTH_SECRET`
- Extract `user_id` from token
- Ensure:
  - Authenticated user ID **matches** `{user_id}` in URL
  - All DB queries filter by `user_id`

Unauthorized → 401  
Wrong user accessing another user’s task → 403/404 per spec

---

### 3. Database Layer
- Use **SQLModel**
- Mirror schema from `specs/database/schema.md`
- Task model fields:
  - id
  - user_id
  - title
  - description
  - completed
  - timestamps

- Store data in Neon PostgreSQL using `DATABASE_URL`.

---

### 4. Code Structure
Recommended:



backend/
main.py
models.py
schemas.py
db.py
auth.py
routes/
tasks.py


---

### 5. Restrictions
You must NOT:
- Modify `/frontend`
- Modify `/specs`
- Change API structure unless specs change
- Ignore authentication

---

## Rules
- Backend code must ALWAYS align with `specs/constitution.md`.
- If specs are unclear, request clarification from Architect or Specs Agent.
