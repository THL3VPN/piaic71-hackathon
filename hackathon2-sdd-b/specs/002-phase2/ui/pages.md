# Phase II UI Pages

All pages must use Better Auth for JWT, attach JWT on API calls, and follow specs in `/specs/002-phase2/ui/components.md`.

- **Login/Signup**
  - Uses Better Auth.
  - On success, stores JWT securely and redirects to Task List.
  - Shows errors for invalid credentials.

- **Task List (Dashboard)**
  - Fetches tasks for authenticated user.
  - Supports mark complete, navigate to create/edit.
  - Shows empty state, loading, and error states.
  - Supports basic filters (status) and respects API pagination defaults.

- **Task Create**
  - Form fields: title (required, ≤200), description (optional, ≤2000).
  - On submit, calls POST `/api/{user_id}/tasks`; handles validation errors.

- **Task Edit**
  - Prefills existing task.
  - Allows update (PUT), delete, and mark complete (PATCH).
  - Handles 401/403/404 gracefully and surfaces actionable messages.
