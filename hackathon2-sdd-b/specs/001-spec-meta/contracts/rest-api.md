# Contracts: REST API (Phase II)

Source of truth: `specs/api/rest-endpoints.md`.

## Summary
- Auth: `Authorization: Bearer <JWT>` required on all endpoints.
- Isolation: `{user_id}` in path must match JWT user_id; otherwise 403/404 per spec.
- Content: JSON requests/responses.
- Validation: title 1..200; description ≤2000.

## Endpoints
- **GET** `/api/{user_id}/tasks` — List tasks; supports status/filter/sort/pagination per API spec.  
- **POST** `/api/{user_id}/tasks` — Create task for user.  
- **GET** `/api/{user_id}/tasks/{id}` — Fetch single task (must belong to user).  
- **PUT** `/api/{user_id}/tasks/{id}` — Replace task fields.  
- **DELETE** `/api/{user_id}/tasks/{id}` — Delete task.  
- **PATCH** `/api/{user_id}/tasks/{id}/complete` — Mark complete (idempotent).

## Status Codes
- Success: 200/201/204 as defined per endpoint.  
- Client errors: 400 validation failures.  
- Auth errors: 401 missing/invalid JWT; 403/404 on cross-user access.  
- Not found: 404 for missing resources (while respecting isolation posture).

## Error Format (recommended)
`{ "error": { "code": "string", "message": "human readable" } }`
