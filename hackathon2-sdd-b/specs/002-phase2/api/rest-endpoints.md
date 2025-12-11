# Phase II API: Task Endpoints

All endpoints:
- Require header: `Authorization: Bearer <JWT>`
- Must enforce user isolation: `{user_id}` in path must match the authenticated user in the JWT. Cross-user access returns 403 (or 404 if hiding existence).
- Return 401 on missing/invalid JWT.

## Models (shared)
- Task fields: `id`, `user_id`, `title`, `description`, `completed`, `created_at`, `updated_at`.
- Title required, trimmed; description optional.

## Endpoints

### GET `/api/{user_id}/tasks`
- Purpose: List tasks for the authenticated user.
- Query params (optional): `status` (pending|done), `limit` (default 50, max 200), `offset` (default 0), `sort` (created_at|updated_at; default created_at desc).
- Responses:
  - 200: `{ "items": [Task], "count": <int> }`
  - 401: missing/invalid JWT
  - 403/404: user mismatch

### POST `/api/{user_id}/tasks`
- Purpose: Create a task for the authenticated user.
- Body: `{ "title": string (1..200), "description": string (0..2000, optional) }`
- Responses:
  - 201: Task object with server `id`, `completed=false`, timestamps.
  - 400: validation errors (too long/empty title).
  - 401: missing/invalid JWT
  - 403/404: user mismatch

### GET `/api/{user_id}/tasks/{id}`
- Purpose: Fetch a single task owned by the user.
- Responses:
  - 200: Task object
  - 401: missing/invalid JWT
  - 403/404: cross-user or not found

### PUT `/api/{user_id}/tasks/{id}`
- Purpose: Replace task title/description/completed flag.
- Body: `{ "title": string (1..200), "description": string (0..2000, optional), "completed": boolean }`
- Responses:
  - 200: Updated Task
  - 400: validation errors
  - 401: missing/invalid JWT
  - 403/404: cross-user or not found

### PATCH `/api/{user_id}/tasks/{id}/complete`
- Purpose: Mark complete (idempotent).
- Body: none
- Responses:
  - 200: Updated Task (`completed=true`)
  - 401: missing/invalid JWT
  - 403/404: cross-user or not found

### DELETE `/api/{user_id}/tasks/{id}`
- Purpose: Delete a task owned by the user.
- Responses:
  - 204: Deleted
  - 401: missing/invalid JWT
  - 403/404: cross-user or not found

## Error format (recommended)
`{ "error": { "code": "string", "message": "human readable" } }`

## Auth expectations
- Backend validates JWT using `BETTER_AUTH_SECRET`.
- Reject expired/invalid tokens with 401.
- All DB queries MUST filter by `user_id` from JWT.
