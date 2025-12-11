# Phase II Database Schema

## Task Table (SQLModel-aligned)
- `id`: UUID (preferred) or serial primary key
- `user_id`: UUID/string (owner), indexed, not null
- `title`: string (1..200), not null
- `description`: string (0..2000), nullable
- `completed`: boolean, default false
- `created_at`: timestamp with time zone, default now()
- `updated_at`: timestamp with time zone, auto-updated

Rules:
- All queries must filter by `user_id` from authenticated JWT.
- No cross-user access; enforce via queries and endpoint checks.
- Schema must match API payloads defined in `/specs/002-phase2/api/rest-endpoints.md`.
- Consider unique index on (`user_id`, `id`) for partitioned access patterns.
