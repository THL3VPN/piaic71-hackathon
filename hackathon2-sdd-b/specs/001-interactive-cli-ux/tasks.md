---

description: "Task list for interactive CLI UX"
---

# Tasks: Interactive CLI UX

**Input**: Design documents from `/home/aie/all_data/piaic71-hackathon/hackathon2-sdd-b/specs/001-interactive-cli-ux/`
**Prerequisites**: plan.md (required), spec.md (user stories), research.md, data-model.md, contracts/

**Tests**: Include pytest tasks needed to keep all tests passing with ≥80% coverage for new/changed code. If a story omits tests, add a task to justify the exception and plan remediation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create CLI directories in `src/cli/` and tests in `tests/` (unit/integration/contract)
- [ ] T002 Add minimal `src/cli/__init__.py` and `src/cli/app.py` Typer app stub
- [ ] T003 Add `tests/conftest.py` with Rich console capture helper and Questionary mock helper
- [ ] T004 Add dev dependencies to `requirements.txt` via `uv pip compile` note in `plan.md` if missing
- [ ] T005 Add coverage config in `pyproject.toml` or `setup.cfg` to enforce ≥80% (document location in plan)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T006 Create `src/cli/prompts.py` with wrapper functions for Questionary (select/text/confirm) plus retry handling
- [ ] T007 Create `src/cli/output.py` with Rich helpers (success, error, table builder) and color-safe fallback
- [ ] T008 Create `src/cli/errors.py` defining user-facing error classes/messages (single-sentence guidance)
- [ ] T009 Wire Typer app entry in `src/cli/main.py` using `app = Typer()` and register placeholder commands
- [ ] T010 Add unit tests for helpers in `tests/unit/test_prompts.py` and `tests/unit/test_output.py`
- [ ] T011 Add unit tests for error formatting in `tests/unit/test_errors.py`
- [ ] T012 Ensure `uv run pytest --cov=app --cov=tests --cov-report=term-missing` documented in `quickstart.md` (update if needed)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Capture tasks interactively (Priority: P1) 🎯 MVP

**Goal**: Add tasks via guided prompts with confirmation

**Independent Test**: Run add command with prompts and confirm task stored with provided values; cancel path leaves no task.

### Tests for User Story 1 ⚠️

- [ ] T013 [P] [US1] Add contract test for `add` command outputs in `tests/contract/test_cli_add.py`
- [ ] T014 [P] [US1] Add integration test for prompt flow and cancel path in `tests/integration/test_cli_add_flow.py`

### Implementation for User Story 1

- [ ] T015 [US1] Implement `add` command in `src/cli/app.py` (Typer command + prompt defaults)
- [ ] T016 [US1] Add interactive prompt flow in `src/cli/prompts.py` for title/priority/notes + confirm
- [ ] T017 [US1] Add service call placeholder/wiring in `src/services/task_service.py` (create task) with stub implementation
- [ ] T018 [US1] Render success/summary via Rich in `src/cli/output.py` for add command
- [ ] T019 [US1] Handle cancel path gracefully in `src/cli/app.py` with friendly message

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Browse and filter tasks visually (Priority: P2)

**Goal**: List tasks with interactive filters and readable tables

**Independent Test**: Run list command, choose filters, and see filtered table; empty state shows friendly message.

### Tests for User Story 2 ⚠️

- [ ] T020 [P] [US2] Add contract test for `list` command output/table columns in `tests/contract/test_cli_list.py`
- [ ] T021 [P] [US2] Add integration test for filter selection and empty-state handling in `tests/integration/test_cli_list_flow.py`

### Implementation for User Story 2

- [ ] T022 [US2] Implement `list` command in `src/cli/app.py` with filter options and prompt fallbacks
- [ ] T023 [US2] Add filter prompt helpers in `src/cli/prompts.py` (priority/status selects with "All")
- [ ] T024 [US2] Add Rich table rendering for tasks in `src/cli/output.py` including empty-state message
- [ ] T025 [US2] Update `src/services/task_service.py` list stub to support filters and return sample data

**Checkpoint**: User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Understand and recover from errors (Priority: P3)

**Goal**: Friendly error reporting and recovery for invalid input/missing data

**Independent Test**: Trigger invalid input; error explains the issue and next step without stack trace.

### Tests for User Story 3 ⚠️

- [ ] T026 [P] [US3] Add contract test for error formatting/messages in `tests/contract/test_cli_errors.py`
- [ ] T027 [P] [US3] Add integration test for invalid priority/missing required fields in `tests/integration/test_cli_error_flows.py`

### Implementation for User Story 3

- [ ] T028 [US3] Implement centralized error handling in `src/cli/app.py` using helpers from `src/cli/errors.py`
- [ ] T029 [US3] Add fallback non-interactive flag validation in `src/cli/app.py` for add/list commands
- [ ] T030 [US3] Ensure Rich error output uses plain-text fallback in `src/cli/output.py`
- [ ] T031 [US3] Add re-prompt logic for invalid selections in `src/cli/prompts.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T032 [P] Add CLI help text review and update `quickstart.md` with examples
- [ ] T033 [P] Add docstring/comments for prompt/output helpers for maintainability in `src/cli/`
- [ ] T034 [P] Add coverage audit and fill gaps in `tests/` if coverage <80%
- [ ] T035 [P] Add deletion safety confirmation copy review in `src/cli/output.py` / `src/cli/prompts.py`

---

## Dependencies & Execution Order

### Phase Dependencies
- Setup (Phase 1) → Foundational (Phase 2) → User stories (Phases 3-5) → Polish
- User stories can start after Foundational completes; they remain independently testable.

### User Story Dependencies
- US1 (P1) has no dependency on other stories.
- US2 (P2) depends on Foundational and can reuse task_service; independent of US1 logic.
- US3 (P3) depends on Foundational and error helpers; can run alongside US2 once helpers exist.

### Parallel Opportunities
- Marked [P] tasks can run in parallel when touching different files (e.g., tests vs helpers).
- Different user story test tasks can proceed in parallel after foundational helpers are ready.

### Implementation Strategy
- Complete Setup → Foundational → US1 (MVP) → US2 → US3 → Polish.
- MVP scope: Finish US1 (add command with prompts/confirmation) with passing tests before continuing.
