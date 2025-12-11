# Feature: Task CRUD (Phase II)

## Goal
Enable authenticated users to manage their own tasks in a multi-user environment with strict user isolation.

## Scope
- Create, read, update, delete tasks.
- Mark tasks complete (idempotent).
- Enforce user isolation on all operations.
- Support filtering, pagination basics, and ordering for list.

## Dependencies
- Auth via Better Auth issuing JWTs.
- API contract: see `/specs/002-phase2/api/rest-endpoints.md`.
- Schema: see `/specs/002-phase2/database/schema.md`.

## Acceptance Criteria
- Users can create tasks scoped to their `user_id` with required title validation (non-empty, length ≤200).
- Listing tasks returns only the authenticated user’s tasks; supports `status`, `limit/offset`, `sort`.
- Updating/deleting/completing rejects cross-user access with 403/404.
- Endpoints require valid JWT; invalid or missing JWT returns 401.
- Mark complete endpoint is idempotent; repeat calls keep `completed=true`.

## Edge Cases
- Empty/whitespace title → 400.
- Title >200 chars or description >2000 chars → 400.
- Missing JWT → 401.
- JWT user_id mismatch → 403/404.
- Nonexistent task id → 404.
