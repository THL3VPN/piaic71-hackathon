---

description: "Task list for Rich/Questionary CLI todo experience"
---

# Tasks: Rich CLI Todo Experience

**Input**: Design documents from `/home/aie/all_data/piaic71-hackathon/hackathon2-sdd/specs/002-rich-cli/`  
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
- Code under `hackathon2-sdd/src/` (cli, lib, services, models)
- Tests under `hackathon2-sdd/tests/` (unit, integration)

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Add dependencies Questionary and Rich via `uv add questionary rich` in /home/aie/all_data/piaic71-hackathon/hackathon2-sdd (deliverable: pyproject/uv.lock updated)
- [X] T002 Ensure CLI entry module exists at hackathon2-sdd/src/cli/main.py and test roots at tests/{unit,integration} (deliverable: directories ready)
- [X] T003 Update AGENTS.md if new commands/tools added (deliverable: agent guidance synced)

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T004 Create/extend validation helpers in hackathon2-sdd/src/lib/validation.py for ids/descriptions (deliverable: typed helpers)
- [X] T005 Stub Rich output helpers in hackathon2-sdd/src/lib/cli_output.py (tables/panels, error panel) (deliverable: helper stubs)
- [X] T006 Add interactive CLI skeleton in hackathon2-sdd/src/cli/interactive.py (Questionary menu placeholders) (deliverable: stub functions)
- [X] T007 Base argparse wiring in hackathon2-sdd/src/cli/main.py for add/view/update/complete/delete + interactive entry (deliverable: argument parsing only)
- [X] T008 Human review checkpoint before user stories (deliverable: approval note in plan.md)

## Phase 3: User Story 1 - Run CLI Operations (Priority: P1) 🎯 MVP

**Goal**: Support add/view/update/complete/delete via args with clear outputs.  
**Independent Test**: Each command with valid input returns exit code 0 and prints expected text/table.

### Tests for User Story 1 (MANDATORY - write before implementation) ⚠️

- [X] T009 [US1] RED: Unit tests for add/update/complete/delete validation and store calls in hackathon2-sdd/tests/unit/test_cli_commands.py (deliverable: failing tests)
- [X] T010 [P] [US1] RED: Integration tests for add/view/update/complete/delete args in hackathon2-sdd/tests/integration/test_cli_commands.py (deliverable: failing tests)

### Implementation for User Story 1

- [X] T011 [US1] Implement argparse handlers in hackathon2-sdd/src/cli/main.py calling services with validation (deliverable: green T009/T010 add/update/complete/delete)
- [X] T012 [US1] Implement plain output path (before Rich) in hackathon2-sdd/src/lib/cli_output.py for commands (deliverable: readable text outputs)
- [ ] T013 [US1] Human review checkpoint for US1 outputs and exit codes; commit or iterate (deliverable: approval + commit note)

## Phase 4: User Story 2 - Interactive Selection & Formatting (Priority: P2)

**Goal**: Add Questionary-driven interactive mode with Rich-formatted outputs.  
**Independent Test**: Interactive add + view completes with two prompts and renders Rich table.

### Tests for User Story 2 (MANDATORY - write before implementation) ⚠️

- [ ] T014 [US2] RED: Unit tests for interactive menu flows in hackathon2-sdd/tests/unit/test_cli_interactive.py (deliverable: failing tests)
- [ ] T015 [US2] RED: Integration test for interactive add+view with Rich table rendering in hackathon2-sdd/tests/integration/test_cli_interactive.py (deliverable: failing test)

### Implementation for User Story 2

- [ ] T016 [US2] Implement interactive menu and prompts in hackathon2-sdd/src/cli/interactive.py (deliverable: green T014/T015)
- [ ] T017 [US2] Implement Rich formatting in hackathon2-sdd/src/lib/cli_output.py (tables/panels) and integrate into main/interactive (deliverable: Rich-rendered outputs)
- [ ] T018 [US2] Human review checkpoint for interactive UX and Rich output; commit or iterate (deliverable: approval + commit note)

## Phase 5: User Story 3 - Errors and Usage Help (Priority: P3)

**Goal**: Provide clear errors/usage on invalid inputs or commands.  
**Independent Test**: Missing args/invalid ids show descriptive errors and usage/help; exit code non-zero.

### Tests for User Story 3 (MANDATORY - write before implementation) ⚠️

- [ ] T019 [US3] RED: Unit tests for validation/error panels and usage printing in hackathon2-sdd/tests/unit/test_cli_errors.py (deliverable: failing tests)
- [ ] T020 [US3] RED: Integration tests for invalid args/unknown commands showing usage/help in hackathon2-sdd/tests/integration/test_cli_usage.py (deliverable: failing tests)

### Implementation for User Story 3

- [ ] T021 [US3] Implement error/usage handling in hackathon2-sdd/src/cli/main.py (argparse hooks, Rich errors) (deliverable: green T019/T020)
- [ ] T022 [US3] Ensure interactive mode handles cancel/invalid input gracefully in hackathon2-sdd/src/cli/interactive.py (deliverable: green T019/T020 for interactive)
- [ ] T023 [US3] Human review checkpoint for error/usage flows; commit or iterate (deliverable: approval + commit note)

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T024 Run full suite with coverage + mypy: `PYTHONPATH=src uv run pytest --cov=src --cov=tests --cov-report=term-missing` and `PYTHONPATH=src uv run mypy src` (deliverable: 100% coverage, clean types)
- [ ] T025 Update docs (quickstart and AGENTS) for interactive/Rich usage in hackathon2-sdd/specs/002-rich-cli/quickstart.md and hackathon2-sdd/AGENTS.md (deliverable: synced docs)
- [ ] T026 [P] Sweep for lint/type/style fixes across hackathon2-sdd/src and hackathon2-sdd/tests (deliverable: clean formatting)
- [ ] T027 Final human review and prepare PR summary (deliverable: approval + ready-to-commit status)

## Dependencies & Execution Order

- Story order: US1 (argparse commands) → US2 (interactive + Rich) → US3 (errors/usage).
- T001–T008 must finish before any US1 tasks. Within each story: RED tests → implement → review.
- T024 depends on all story tasks complete.

## Parallel Example

- T009 and T010 can be written in parallel (different test files).
- T014 and T015 can be written in parallel once US1 is done.
- T019 and T020 can be written in parallel.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup + Foundational (T001–T008).
2. Finish US1 tasks (T009–T013) for basic CLI operations.
3. Review/commit before interactive/Rich work.

### Incremental Delivery

1. Setup + Foundational → foundation ready.
2. US1 → review/commit.
3. US2 → review/commit.
4. US3 → review/commit.

### Parallel Team Strategy

- Parallelize RED tests within a story (T009/T010, T014/T015, T019/T020).
- Implementations follow serialized per story after tests to respect TDD.
