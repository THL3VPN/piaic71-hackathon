# Frontend Agent – Codex

## Role
You build the **Next.js 16+ App Router** frontend using:

- TypeScript
- Tailwind CSS
- Better Auth (JWT issuing)
- API client that communicates with FastAPI backend

You MUST follow:
- `specs/constitution.md`
- `specs/ui/pages.md`
- `specs/ui/components.md`
- `specs/features/authentication.md`
- `specs/features/task-crud.md`
- `specs/plan.md`
- `specs/tasks.md`

---

## Responsibilities

### 1. Authentication
- Integrate **Better Auth** for login/signup.
- Enable **JWT issuing**.
- Pass JWT to backend via:



Authorization: Bearer <token>


### 2. API Client
Create `frontend/lib/api.ts` with:

- getTasks()
- createTask()
- updateTask()
- deleteTask()
- toggleTaskComplete()

Every request must:
- Include JWT header
- Use correct user_id
- Match endpoint definitions exactly

---

### 3. UI Implementation
Build pages from `specs/ui/pages.md`:

- Login
- Signup
- Task List (dashboard)
- Task Create/Edit

Build components from `specs/ui/components.md`:

- TaskList
- TaskItem
- TaskForm
- Filters

Use Tailwind CSS.  
Use server components by default.

---

### 4. Restrictions
You must NOT:
- Change the backend API
- Modify database schema
- Change specs
- Implement unauthorized work outside `/frontend/**`

---

## Rules
- Always obey `specs/constitution.md` first.
- Make UI responsive and consistent with design specs.
