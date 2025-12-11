# Phase II API: Task Endpoints

Required endpoints (JWT-protected, user-isolated):
- GET    `/api/{user_id}/tasks`
- POST   `/api/{user_id}/tasks`
- GET    `/api/{user_id}/tasks/{id}`
- PUT    `/api/{user_id}/tasks/{id}`
- DELETE `/api/{user_id}/tasks/{id}`
- PATCH  `/api/{user_id}/tasks/{id}/complete`

Auth & isolation:
- `Authorization: Bearer <token>` required on every request.
- `{user_id}` in path must match the authenticated user.
- Reject unauthorized access; no user may access another user’s tasks.

Request/response shapes and status codes must match the detailed API spec (to be expanded here per Constitution and Phase II plan).
