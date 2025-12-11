# Contracts: REST API (Phase II)

Source of truth: `specs/002-phase2/api/rest-endpoints.md`.

## Summary
- Auth: `Authorization: Bearer <JWT>` required on all endpoints.
- Isolation: `{user_id}` path must match JWT user_id; otherwise 403/404.
- Validation: title 1..200 chars; description ≤2000.

## Endpoints (high level)
- GET `/api/{user_id}/tasks` — list with status filter, pagination (limit/offset), sort.
- POST `/api/{user_id}/tasks` — create task.
- GET `/api/{user_id}/tasks/{id}` — fetch single task.
- PUT `/api/{user_id}/tasks/{id}` — replace fields.
- PATCH `/api/{user_id}/tasks/{id}/complete` — mark complete (idempotent).
- DELETE `/api/{user_id}/tasks/{id}` — delete task.

## Status Codes
- 200/201/204 success variants
- 400 validation errors
- 401 missing/invalid JWT
- 403/404 cross-user or missing resource
