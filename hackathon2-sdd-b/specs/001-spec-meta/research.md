# Phase II Research (Meta-Spec)

## Decisions

- **Stack enforcement**: Use Next.js 16+ (App Router) with Tailwind and Better Auth on frontend; FastAPI + SQLModel with Neon PostgreSQL on backend.  
  - Rationale: Matches Constitution v3.0.0 and Phase II objectives; supports JWT auth and multi-user isolation.  
  - Alternatives: Other stacks (rejected per Constitution).
- **Auth model**: Better Auth issues JWT; FastAPI validates with `BETTER_AUTH_SECRET`; enforce `{user_id}` match on every request.  
  - Rationale: Required by spec; ensures user isolation.  
  - Alternatives: Session cookies (rejected: not aligned with API/JWT mandate).
- **REST contract stability**: Preserve canonical endpoints under `/api/{user_id}/tasks` including PATCH complete.  
  - Rationale: Contract defined in specs; needed for frontend integration and Phase III extensions.  
  - Alternatives: GraphQL or altered routes (rejected: violates spec).
- **Manual local dev (no Docker)**: Run backend via `uvicorn` and frontend via `npm run dev`; manage env vars manually.  
  - Rationale: User directive; simplifies Phase II setup.  
  - Alternatives: Docker-compose (rejected for this phase).
- **Data ownership enforcement**: All DB queries filter by authenticated `user_id`; mismatch returns 403/404 per spec.  
  - Rationale: Prevents cross-user leakage; required by Constitution.  
  - Alternatives: None acceptable.

## Open Questions

- None; requirements are explicit (stack, auth, endpoints, no Docker).

## References

- Constitution v3.0.0  
- specs/001-spec-meta/spec.md  
- specs/api/rest-endpoints.md (referenced contract)  
- specs/database/schema.md (referenced task model)
