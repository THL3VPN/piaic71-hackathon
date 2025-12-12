# Quickstart (Phase II, No Docker)

## Prerequisites
- Python 3.12+
- `uv` installed
- Node.js (Next.js 16+)
- Environment variables: `DATABASE_URL`, `BETTER_AUTH_SECRET`
- Frontend API base: `NEXT_PUBLIC_API_URL` (e.g., http://localhost:8000)

## Backend (FastAPI + SQLModel)
```bash
cd backend
uv run -m pip install -r requirements.txt
uv run -m uvicorn main:app --reload --port 8000
```

Ensure `DATABASE_URL` points to Neon PostgreSQL and is exported in the shell (or .env loaded manually).

## Frontend (Next.js + Better Auth)
```bash
cd frontend
npm install
npm run dev
```

Ensure frontend env points API calls to `http://localhost:8000` and includes `BETTER_AUTH_SECRET`/auth config as required by Better Auth.

## Notes
- JWT must be attached to all API requests: `Authorization: Bearer <token>`.
- Backend must validate JWT with `BETTER_AUTH_SECRET` and enforce `{user_id}` ownership.
- Manual local dev only; Docker is intentionally excluded in Phase II.
- Sample .env.example (root):
  ```
  DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/dbname
  BETTER_AUTH_SECRET=replace-with-secret
  NEXT_PUBLIC_API_URL=http://localhost:8000
  ```
- E2E sanity: login/signup → obtain JWT → CRUD tasks (create/list/update/delete/toggle) → logout; user A must not see user B tasks.
