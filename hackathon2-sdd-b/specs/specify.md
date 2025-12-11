# Meta-Specification: hackathon-todo

This document explains how the `hackathon-todo` project is organized under Spec-Kit and how Codex agents must interpret, load, and use the specifications. It defines:
- The purpose of specifications
- How specs relate to the Constitution, Plan, and Tasks
- How multi-agent Codex development should operate
- How phases progress
- Where specs must be stored and how they should be referenced

The `/specs` directory is the **authoritative source of truth** for the functional and technical behavior of the system. Specifications define **WHAT** the software must do, not HOW it must be implemented. All Codex agents — Architect, Backend, Frontend, Specs, DevOps — must treat `/specs` as the primary reference when generating, modifying, or validating code. A separate **Constitution file** defines the global governing project rules and has higher priority than individual specs.

## Spec Structure

```text
/specs
  specify.md           – This meta-spec (how specs work)
  plan.md              – Execution strategy for the current phase
  tasks.md             – Actionable checklist for agents
  overview.md          – High-level project overview
  architecture.md      – System architecture description
  /features            – Feature-level functional requirements
  /api                 – REST API specifications
  /database            – Schema definitions
  /ui                  – UI layout & components
```

Each area has a clear purpose:

| Location              | Purpose                                           |
|-----------------------|---------------------------------------------------|
| specify.md            | How Spec-Kit and specs should be used             |
| plan.md               | Overall implementation plan                       |
| tasks.md              | Execution steps for Codex agents                  |
| overview.md           | Context and product vision                        |
| architecture.md       | System-level structure & patterns                 |
| features/*.md         | User stories & feature requirements               |
| api/*.md              | Endpoint definitions & contracts                  |
| database/schema.md    | Data model and persistence layer structure        |
| ui/*.md               | Screens, flows, and UI components                 |

Specs under `/specs/features`, `/specs/api`, `/specs/database`, and `/specs/ui` must not contain implementation code.

## Phases in Spec-Kit

The project is organized into phases (configured in `.spec-kit/config.yaml`):
- Phase I – Console application (completed)
- Phase II – Full-stack web application (current)
- Phase III – Chatbot integration (future)

Codex agents must always focus on the currently active phase (Phase II for now). Features are associated with phases in `.spec-kit/config.yaml`.

## Priority Order for Rules

Codex agents must obey rules in the following order:
1) Constitution file (global governing rules)  
2) plan.md (how to implement the current phase)  
3) tasks.md (what to do, step by step)  
4) Specs in `/specs`:  
   - `/specs/features/*.md`  
   - `/specs/api/*.md`  
   - `/specs/database/*.md`  
   - `/specs/ui/*.md`  
5) Agent-level instructions (files under `/agents`)  
6) Local folder-level instructions (e.g., `backend/CODEX.md`, `frontend/CODEX.md`)  

If a conflict occurs: the Constitution overrides everything. Then `plan.md` overrides `tasks.md`. Specs override any agent-local instruction. Agents must never ignore the Constitution, Plan, or Tasks.

## How Agents Use Specs

### Architect Agent
Ensures that folder structure, architecture, and technology choices align with all specs and the Constitution. May propose spec changes, which must be applied through the Specs Agent.

### Backend Agent
Reads feature, API, and database specs before implementing or changing backend code. Must follow API contracts and data models defined under `/specs/api` and `/specs/database`. Treats specs as read-only; it does not modify them.

### Frontend Agent
Reads feature and UI specs (and API specs where relevant) before building or changing frontend code. Must follow UI layouts and flows defined under `/specs/ui`. Treats specs as read-only; it does not modify them.

### Specs Agent
The only agent allowed to modify files under `/specs`. Keeps specs accurate and synchronized with actual behavior. Updates specs when requirements or architecture change.

### DevOps Agent
Reads specs to understand services, environment, and integration requirements. Does not modify specs; uses them to configure infra and tooling.

## Referencing Specs

Codex agents should reference spec files by their Spec-Kit paths, for example:
- `@specs/features/task-crud.md`
- `@specs/features/authentication.md`
- `@specs/api/rest-endpoints.md`
- `@specs/database/schema.md`
- `@specs/ui/pages.md`
- `@specs/ui/components.md`

Before implementing or modifying a feature, endpoint, schema, or UI, agents must first read the relevant spec file(s).

## Enforcement of Spec-Driven Development

To maintain a spec-driven workflow:
- Code must not contradict specs.
- If requirements change: Specs Agent updates the relevant spec(s). Then implementation agents adjust code to match.
- Backend and frontend must:
  - Match the REST API definitions exactly (paths, methods, request/response shapes, auth behavior).
  - Use database fields and relations as defined in the schema specs.
  - Implement UI behavior as described in the UI specs.

If code and specs diverge: prefer to bring code back in line with specs. If the spec is outdated, the Specs Agent updates it and clearly describes the change.

## JWT, Auth, and API-Level Rules

For Phase II:
- All REST API endpoints must follow the authentication and user-isolation rules defined in the Constitution and related API specs.
- Backend must: validate JWT tokens using a shared secret (e.g., `BETTER_AUTH_SECRET`); enforce that users only access their own data.
- Frontend must: use the configured auth library (Better Auth) to acquire JWTs; attach JWTs to all authenticated API requests.
- API specs under `/specs/api` define: required headers, expected status codes, request/response formats. Agents must implement and test behavior according to those specs.

## Future Extensions

This meta-spec is designed to support future phases (e.g., chatbot, MCP tools, extended APIs) without breaking existing Phase II behavior. When new capabilities are added:
- New spec files may be created under `/specs/features`, `/specs/api`, `/specs/database`, or `/specs/ui`.
- The Specs Agent ensures backward compatibility where possible.
- The Constitution and Plan are updated as needed, via the Specs Agent.

## Permissions and Edit Policy

Only the Specs Agent is allowed to modify files under `/specs`, including:
- `specify.md`
- `plan.md`
- `tasks.md`
- `overview.md`
- `architecture.md`
- All files under `features/`, `api/`, `database/`, `ui/`

Backend, Frontend, Architect, and DevOps agents must treat `/specs` as read-only. Any change to specs should reflect actual or planned changes to system behavior, not arbitrary edits.
