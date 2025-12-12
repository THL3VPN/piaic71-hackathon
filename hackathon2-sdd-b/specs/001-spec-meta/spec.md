# Feature Specification: Spec-Kit Meta Governance

**Feature Branch**: `001-spec-meta`  
**Created**: 2025-12-12  
**Status**: Draft  
**Input**: User description: "Define how hackathon-todo specs are organized under Spec-Kit, how Codex agents read/apply them, rule priority, directory structure, phase progression, and enforcement (Phase II: full-stack web app with JWT, REST, and user isolation)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Agents orient to rules (Priority: P1)

An Architect or implementation agent needs to quickly understand the authoritative rule order (Constitution → plan → tasks → specs) and where to find the current phase specs before starting work.

**Why this priority**: Correct rule ordering prevents misaligned implementation and rework.

**Independent Test**: After reading the meta-spec, an agent can list the rule priority and the exact `/specs` paths to consult for Phase II without outside help.

**Acceptance Scenarios**:

1. **Given** an agent preparing to start a task, **When** they read the meta-spec, **Then** they identify the current phase (Phase II) and the required spec folders to consult.  
2. **Given** a conflict between tasks and plan, **When** the agent consults the rule order, **Then** they choose the higher-priority source (plan over tasks) without ambiguity.

---

### User Story 2 - Specs ownership and edit policy (Priority: P2)

The Specs Agent must know it alone can edit specs, while other agents recognize specs as read-only and route changes through the Specs Agent.

**Why this priority**: Protects the source of truth from unauthorized edits.

**Independent Test**: A Backend agent attempting to change `/specs/api` is redirected to the Specs Agent per the meta-spec; the Specs Agent can enumerate its edit scope.

**Acceptance Scenarios**:

1. **Given** a requested change to API contracts, **When** the Specs Agent follows the meta-spec, **Then** it updates the relevant files and informs implementation agents to align code.  
2. **Given** a Frontend agent tries to edit `/specs/ui`, **When** they check the meta-spec, **Then** they see the edit restriction and defer to the Specs Agent.

---

### User Story 3 - Enforcement of Phase II security and contracts (Priority: P3)

Agents need to understand Phase II mandates: stable REST endpoints, JWT on all requests, and strict user isolation.

**Why this priority**: Ensures security and contract fidelity across frontend and backend.

**Independent Test**: An agent can restate required endpoints, auth headers, and isolation rules before coding or reviewing.

**Acceptance Scenarios**:

1. **Given** a developer implementing an endpoint, **When** they consult the meta-spec, **Then** they enforce `Authorization: Bearer <token>` and `{user_id}` ownership for all task routes.  
2. **Given** a UI change, **When** the agent reads the meta-spec, **Then** they attach JWTs to backend calls and follow the referenced API/UI specs.

### Edge Cases

- Conflicts between Constitution, plan, tasks, or agent-local instructions.  
- Missing or outdated spec files or phase mappings.  
- Unauthorized spec edits by non-Specs agents.  
- Phase transition while the meta-spec remains in circulation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The meta-spec MUST declare `/specs` as the authoritative source of truth and describe the purpose of specifications (WHAT, not HOW).  
- **FR-002**: The meta-spec MUST define the `/specs` structure and the purpose of each file/folder (specify.md, plan.md, tasks.md, overview.md, architecture.md, features/, api/, database/, ui/).  
- **FR-003**: The meta-spec MUST state the rule priority order: Constitution → plan.md → tasks.md → specs (features/api/database/ui) → /agents → local CODEX/agent files; include conflict resolution.  
- **FR-004**: The meta-spec MUST describe Phase I (completed) and Phase II (current) and require agents to operate according to the active phase and `.spec-kit/config.yaml` mappings.  
- **FR-005**: The meta-spec MUST define agent responsibilities and edit permissions: Specs Agent is the only editor of `/specs`; Architect guides alignment; Backend/Frontend read specs and implement; DevOps reads specs for infra; none except Specs Agent may edit specs.  
- **FR-006**: The meta-spec MUST require agents to reference specs via Spec-Kit paths and read relevant specs before generating or modifying code.  
- **FR-007**: The meta-spec MUST enforce Phase II security and contract rules: JWT on all API requests, shared-secret verification, `{user_id}` ownership checks, and stable REST endpoints as listed.  
- **FR-008**: The meta-spec MUST require code to align to specs and define divergence handling: prefer changing code to match specs; only Specs Agent updates specs when requirements change.  
- **FR-009**: The meta-spec MUST prohibit implementation code inside specs.  
- **FR-010**: The meta-spec MUST support future extensions (e.g., chatbot, MCP tools, additional APIs/UI) by expanding specs and updating Constitution/Plan as needed.

### Key Entities *(include if feature involves data)*

- **Specification**: Authoritative description of functional/technical behavior organized under `/specs`.  
- **Constitution**: Highest-priority governance rules for the project.  
- **Phase**: Active delivery stage (currently Phase II) that scopes applicable specs and tasks.  
- **Agent Role**: Codex roles (Architect, Backend, Frontend, Specs, DevOps) and their permissions/responsibilities relative to specs.

## Edit Policy & Rule Priority Summary

- Rule order: Constitution → plan.md → tasks.md → specs (features/api/database/ui) → /agents → local files.  
- Specs are read-only for all except the Specs Agent.  
- Backend/Frontend/DevOps/Architect must read relevant specs before changing code or structure.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of agents can list the rule priority and active phase after reading the meta-spec (spot-check/orientation).  
- **SC-002**: 0 unauthorized spec edits by non-Specs agents during Phase II reviews.  
- **SC-003**: 100% of new or updated API/UI/DB changes cite the relevant `/specs` paths before implementation.  
- **SC-004**: All task/plan conflicts are resolved by applying the documented rule order (no unaddressed discrepancies in reviews).  
- **SC-005**: All Phase II API calls in code reviews show JWT attachment and user-id ownership enforcement per the referenced specs.
