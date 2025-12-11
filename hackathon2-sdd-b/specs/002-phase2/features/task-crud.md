# Feature: Task CRUD (Phase II)

## Goal
Enable authenticated users to manage their own tasks in a multi-user environment.

## Scope
- Create, read, update, delete tasks.
- Mark tasks complete.
- Enforce user isolation on all operations.

## Dependencies
- Auth via Better Auth issuing JWTs.
- API contract: see `/phase2/api/rest-endpoints.md`.
- Schema: see `/phase2/database/schema.md`.

## Acceptance Criteria
- Users can create tasks scoped to their user_id.
- Listing tasks returns only the authenticated user’s tasks.
- Updating/deleting/completing rejects cross-user access.
- Endpoints require valid JWT; invalid or missing JWT returns 401.
