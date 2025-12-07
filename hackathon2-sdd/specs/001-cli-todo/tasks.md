---

description: "Task list for CLI Todo App implementation"
---

# Tasks: CLI Todo App

**Input**: Design documents from `/home/aie/all_data/piaic71-hackathon/hackathon2-sdd/specs/001-cli-todo/`  
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are MANDATORY under the constitution. Write pytest tasks first for each story, ensure
they fail before implementation, and target 100% coverage with mypy passing.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project rooted at `hackathon2-sdd/`
- Code under `hackathon2-sdd/src/` (models, services, cli, lib)
- Tests under `hackathon2-sdd/tests/` (unit, integration)

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Initialize project in hackathon2-sdd using `uv init` and ensure src/{cli,models,services,lib} plus tests/{unit,integration} exist (deliverable: uv-initialized project layout)
- [X] T002 Initialize uv environment and sync deps via `uv sync` at /home/aie/all_data/piaic71-hackathon/hackathon2-sdd (deliverable: up-to-date .venv)
- [X] T003 Add pytest and mypy config stubs in hackathon2-sdd/pyproject.toml if missing (deliverable: configs align with 100% coverage + type checks)
- [X] T004 Document Context7 MCP usage plan in hackathon2-sdd/specs/001-cli-todo/research.md addendum (deliverable: note to pull docs via MCP where available)

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T005 Create task dataclass scaffold in hackathon2-sdd/src/models/task.py with type hints only (no logic) (deliverable: dataclass placeholder)
- [X] T006 Stub in-memory store interface in hackathon2-sdd/src/services/store.py with function signatures only (add/find/update/delete) (deliverable: typed interfaces)
- [X] T007 Prepare base test helpers for CLI output capture in hackathon2-sdd/tests/conftest.py (deliverable: reusable fixtures)
- [X] T008 Human review checkpoint: confirm foundations and TDD plan before user stories (deliverable: approval note in plan.md)

## Phase 3: User Story 1 - Capture and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Add tasks with descriptions and view all with ids/status.  
**Independent Test**: After completing this phase, `add` then `view` shows the created task with pending status.

### Tests for User Story 1 (MANDATORY - write before implementation) ⚠️

- [X] T009 [US1] RED: Write unit tests for add_task behavior in hackathon2-sdd/tests/unit/test_tasks_add.py (deliverable: failing tests)
- [X] T010 [P] [US1] RED: Write unit tests for view_tasks listing in hackathon2-sdd/tests/unit/test_tasks_view.py (deliverable: failing tests)
- [X] T011 [US1] RED: Write integration test for CLI add+view flow in hackathon2-sdd/tests/integration/test_cli_add_view.py (deliverable: failing test)

### Implementation for User Story 1

- [X] T012 [US1] Implement add_task in hackathon2-sdd/src/services/store.py to append Task with new id (deliverable: green T009)
- [X] T013 [US1] Implement view_tasks in hackathon2-sdd/src/services/store.py returning ordered tasks (deliverable: green T010)
- [X] T014 [US1] Wire CLI subcommands add/view in hackathon2-sdd/src/cli/main.py using argparse (deliverable: green T011)
- [X] T015 [US1] Refactor for duplication removal and functional purity where possible in hackathon2-sdd/src/services/store.py (deliverable: clean code post-green)
- [ ] T016 [US1] Update docs/quickstart with add/view examples in hackathon2-sdd/specs/001-cli-todo/quickstart.md (deliverable: updated guide)
- [ ] T017 [US1] Human review checkpoint: present US1 changes; on approval, commit or iterate (deliverable: approval + commit/changes)

## Phase 4: User Story 2 - Update and Complete Tasks (Priority: P2)

**Goal**: Update descriptions and mark tasks complete by id.  
**Independent Test**: After completion, update then view reflects new description; complete then view shows completed status.

### Tests for User Story 2 (MANDATORY - write before implementation) ⚠️

- [X] T018 [US2] RED: Unit tests for update_task validation and behavior in hackathon2-sdd/tests/unit/test_tasks_update.py (deliverable: failing tests)
- [X] T019 [US2] RED: Unit tests for complete_task idempotency in hackathon2-sdd/tests/unit/test_tasks_complete.py (deliverable: failing tests)
- [X] T020 [US2] RED: Integration test CLI update+complete flow in hackathon2-sdd/tests/integration/test_cli_update_complete.py (deliverable: failing test)

### Implementation for User Story 2

- [X] T021 [US2] Implement update_task in hackathon2-sdd/src/services/store.py (deliverable: green T018)
- [X] T022 [US2] Implement complete_task with idempotent handling in hackathon2-sdd/src/services/store.py (deliverable: green T019)
- [X] T023 [US2] Wire CLI subcommands update/complete in hackathon2-sdd/src/cli/main.py (deliverable: green T020)
- [X] T024 [US2] Refactor shared validation/formatting into hackathon2-sdd/src/lib/validation.py (deliverable: reduced duplication)
- [X] T025 [US2] Human review checkpoint: present US2 changes; on approval, commit or iterate (deliverable: approval + commit/changes)

## Phase 5: User Story 3 - Remove Tasks (Priority: P3)

**Goal**: Delete tasks by id and confirm removal.  
**Independent Test**: After completion, delete then view omits the task and preserves ids.

### Tests for User Story 3 (MANDATORY - write before implementation) ⚠️

- [X] T026 [US3] RED: Unit tests for delete_task behavior in hackathon2-sdd/tests/unit/test_tasks_delete.py (deliverable: failing tests)
- [X] T027 [US3] RED: Integration test CLI delete flow in hackathon2-sdd/tests/integration/test_cli_delete.py (deliverable: failing test)

### Implementation for User Story 3

- [X] T028 [US3] Implement delete_task in hackathon2-sdd/src/services/store.py (deliverable: green T026)
- [X] T029 [US3] Wire CLI delete subcommand in hackathon2-sdd/src/cli/main.py (deliverable: green T027)
- [X] T030 [US3] Refactor common CLI messaging and exit handling in hackathon2-sdd/src/lib/cli_output.py (deliverable: consistent outputs)
- [X] T031 [US3] Human review checkpoint: present US3 changes; on approval, commit or iterate (deliverable: approval + commit/changes)

## Phase N: Polish & Cross-Cutting Concerns

- [X] T032 Run full suite with coverage + mypy: `uv run pytest --cov=src --cov=tests --cov-report=term-missing` and `uv run mypy src` (deliverable: 100% coverage, clean types)
- [X] T033 Add README/usage snippet updates in hackathon2-sdd/specs/001-cli-todo/quickstart.md and hackathon2-sdd/AGENTS.md (deliverable: synced docs)
- [X] T034 [P] Sweep for lint/type/style fixes across hackathon2-sdd/src and hackathon2-sdd/tests (deliverable: clean formatting)
- [X] T035 Final human review and prepare PR summary (deliverable: approval + ready-to-commit status)

## Dependencies & Execution Order

- Story order: US1 (add/view) → US2 (update/complete) → US3 (delete).
- T001–T008 must finish before any US1 tasks. Within each story: RED tests → implement → refactor → human review.
- T032 depends on completion of all story tasks.

## Parallel Example

- Run T009 and T010 in parallel (different test files) before implementation.
- While T012 runs, T011 can be prepped but remains failing until CLI wiring (T014) completes.
- In US2, T018 and T019 can proceed in parallel; same for T026 and T027 in US3.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup + Foundational (T001–T008).
2. Finish US1 tasks (T009–T017).
3. Pause for review/commit; CLI supports add/view.

### Incremental Delivery

1. Setup + Foundational → foundation ready.
2. Add US1 → review/commit.
3. Add US2 → review/commit.
4. Add US3 → review/commit.

### Parallel Team Strategy

- Split RED test writing per story across contributors.
- Keep implementation per story serialized after tests to respect dependencies and TDD sequencing.
