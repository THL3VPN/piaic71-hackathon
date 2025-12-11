# Feature: Authentication (Phase II)

## Goal
Provide signup/signin via Better Auth, issuing JWTs for authenticated access to the task API.

## Scope
- User signup and signin flows via Better Auth.
- Issue JWT containing `user_id` for backend authorization.
- Frontend must store and send JWT on every authenticated API call.

## Dependencies
- Better Auth service/library (frontend).
- Backend JWT validation via `BETTER_AUTH_SECRET`.
- API contract: see `/specs/002-phase2/api/rest-endpoints.md` for auth expectations.

## Acceptance Criteria
- Users can signup/signin and receive a JWT that includes their `user_id`.
- Frontend attaches `Authorization: Bearer <token>` to all API calls.
- Backend rejects missing/invalid/expired tokens with 401.
- Backend enforces path `{user_id}` matches JWT user_id (403/404 otherwise).

## Edge Cases
- Expired or tampered token → 401.
- Token user_id mismatch with path → 403/404.
- Logout clears stored JWT on frontend.
