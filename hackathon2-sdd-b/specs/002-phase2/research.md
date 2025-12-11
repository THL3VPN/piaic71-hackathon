# Phase II Research

## Decisions
- **JWT via Better Auth**: Use Better Auth to issue JWTs containing `user_id`; backend validates with `BETTER_AUTH_SECRET`.
  - Rationale: Aligns with Constitution and Phase II specs; reduces custom auth risk.
  - Alternatives: Custom JWT issuer (rejected: more boilerplate, higher risk).
- **User Isolation**: Enforce `{user_id}` path match + DB filtering by JWT `user_id`.
  - Rationale: Mandatory per Constitution; prevents data leakage.
  - Alternatives: Global multi-tenant queries without path match (rejected: violates specs).
- **Neon PostgreSQL**: Use `DATABASE_URL` for SQLModel engine.
  - Rationale: Required stack; serverless Postgres fits multi-env needs.
  - Alternatives: Local SQLite (rejected: not aligned with Neon requirement).
- **Request Validation**: Pydantic schemas enforce title (1..200) and description (≤2000).
  - Rationale: Matches API and feature specs; predictable 400 responses.
  - Alternatives: Lenient validation (rejected: spec noncompliance).
- **Backend async FastAPI/SQLModel**: Use async engine/session for scalability.
  - Rationale: Better I/O concurrency; compatible with FastAPI.
  - Alternatives: Sync engine (acceptable fallback if complexity arises).
- **Pagination defaults**: limit default 50, max 200; sort by created_at desc.
  - Rationale: Matches API spec and keeps responses lightweight.
  - Alternatives: Unlimited listings (rejected: performance risk).
- **HTTP status policy**: 401 for missing/invalid JWT; 403/404 for cross-user depending on leak posture.
  - Rationale: Spec-compliant; hides existence when appropriate.
  - Alternatives: 403 always (acceptable variant; choose consistent approach).

## Open Questions
- None marked as NEEDS CLARIFICATION at this stage.

## References
- Constitution v2.0.0 (Phase II full-stack rules)
- Specs in `specs/002-phase2` (API, features, database, UI)
