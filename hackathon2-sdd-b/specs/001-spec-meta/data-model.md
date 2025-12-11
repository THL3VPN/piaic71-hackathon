# Data Model (Phase II Meta-Spec)

## Entities

### Task
- id: UUID (primary key)
- user_id: UUID/string (owner, indexed)
- title: string (required; 1..200 chars)
- description: string (optional; ≤2000 chars)
- completed: boolean (default false)
- created_at: timestamp with time zone (default now)
- updated_at: timestamp with time zone (auto-updated)

## Rules

- Ownership: All CRUD operations filter by `user_id` matching the authenticated user (from JWT).  
- Validation: Enforce title length and description max length.  
- Pagination/Sorting: Support limit/offset and sort by created_at/updated_at as defined in API specs.  
- Indexing: Add index on `user_id` for isolation and query performance.
