# Phase II Database Schema

## Task Table (SQLModel-aligned)
- id (UUID or serial)
- user_id (UUID/string) — owner; indexed
- title (string)
- description (string, optional)
- completed (boolean)
- created_at (timestamp)
- updated_at (timestamp)

Rules:
- All queries must filter by `user_id` from authenticated JWT.
- No cross-user access.
- Schema must match API payloads defined in `/phase2/api/rest-endpoints.md`.
