# Quickstart (Phase II)

## Prerequisites
- Python 3.12+
- `uv` installed
- Node.js (for Next.js)
- Environment variables: `DATABASE_URL`, `BETTER_AUTH_SECRET`

## Backend
```bash
uv run -m pip install -r requirements.txt
uv run -m uvicorn backend.main:app --reload
```

## Frontend
```bash
cd frontend
npm install
npm run dev
```

## Notes
- Ensure `DATABASE_URL` points to Neon PostgreSQL.
- All API calls require `Authorization: Bearer <token>` with Better Auth JWT.
