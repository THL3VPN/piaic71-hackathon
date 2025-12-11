# Data Model (Phase II)

## Entities

### Task
- id: UUID (pk)
- user_id: UUID/string (owner, indexed)
- title: string (required, 1..200)
- description: string (optional, ≤2000)
- completed: boolean (default false)
- created_at: timestamp with time zone (default now)
- updated_at: timestamp with time zone (auto-updated)

## Rules
- All CRUD operations filter by `user_id` from JWT.
- Validation: enforce title length and description max length.
- Sorting/pagination: support limit/offset and sort by created_at/updated_at.
