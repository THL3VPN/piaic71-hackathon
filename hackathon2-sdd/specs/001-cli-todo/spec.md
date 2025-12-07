# Feature Specification: Command-line Todo App

**Feature Branch**: `[001-cli-todo]`  
**Created**: 2025-12-06  
**Status**: Draft  
**Input**: User description: "Feature: Build a command-line todo application that stores tasks in memory User journeys: - Add a task - Delete a task - Update a task - view a task - Mark Complete a task Acceptance criteria: - All operations work correct formating and input type as string - All operations return correct results - All operations have full test coverage - All functions use Python 3.13+ type hints - All functions have clear docstrings Success metrics: - 100% test coverage for all operations - Type checking passes with mypy - Code follows our constitution rules"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Capture and View Tasks (Priority: P1)

Users add a todo item with a description and immediately see it listed with a unique identifier and
pending status.

**Why this priority**: Core flow that establishes the todo list and confirms tasks are tracked.

**Independent Test**: Add a task via CLI, then view tasks to verify the new item appears with correct
id, description, and status.

**Acceptance Scenarios**:

1. **Given** no tasks exist, **When** the user adds "Buy milk", **Then** the list shows one task with
   a unique id, description "Buy milk", and status "pending".
2. **Given** an existing task, **When** the user runs view, **Then** all tasks display with ids and
   statuses in a readable format.

---

### User Story 2 - Update and Complete Tasks (Priority: P2)

Users refine a task’s description or mark it complete to reflect progress.

**Why this priority**: Keeps tasks accurate and signals completion, reducing confusion.

**Independent Test**: Update a task description, then mark it complete; view confirms the new text
and completed status.

**Acceptance Scenarios**:

1. **Given** a task with id 1, **When** the user updates its description to "Buy oat milk", **Then**
   viewing shows id 1 with description "Buy oat milk" and status unchanged.
2. **Given** a pending task with id 1, **When** the user marks it complete, **Then** viewing shows id
   1 with status "completed".

---

### User Story 3 - Remove Tasks (Priority: P3)

Users delete tasks they no longer need so the list stays current.

**Why this priority**: Prevents clutter and keeps focus on active tasks.

**Independent Test**: Delete a task by id; viewing confirms it no longer appears.

**Acceptance Scenarios**:

1. **Given** a task with id 1, **When** the user deletes it, **Then** viewing shows the task is
   absent and remaining tasks keep their ids.

### Edge Cases

- Adding an empty or whitespace-only description is rejected with a clear error.
- Viewing when no tasks exist returns an empty list message (not an error).
- Updating, completing, or deleting a non-existent id returns a clear not-found message.
- Duplicate descriptions are allowed but each task retains a unique id.
- Marking an already completed task reports that it is already complete without altering data.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Users MUST add a task with a non-empty string description; the system assigns a unique
  id and sets status to "pending".
- **FR-002**: Users MUST view all tasks with id, description, and status presented in readable
  format; ordering remains consistent across operations.
- **FR-003**: Users MUST update a task’s description by id using a string input without changing its
  status.
- **FR-004**: Users MUST mark a task complete by id; status changes to "completed" and is visible on
  subsequent views.
- **FR-005**: Users MUST delete a task by id; deleted tasks are removed from the current session’s
  in-memory list.
- **FR-006**: All operations MUST validate inputs as strings and return descriptive error messages
  for invalid or missing data.
- **FR-007**: Command responses MUST indicate success or failure with the affected task id and
  current state when applicable.
- **FR-008**: The in-memory store MUST reflect changes immediately for add, update, complete, and
  delete actions within the session.
- **FR-009**: Quality gates: every function MUST have type hints and docstrings; tests MUST cover all
  operations with 100% coverage; static type checks MUST pass without errors.

### Key Entities *(include if feature involves data)*

- **Task**: Represents a todo item with attributes: `id` (unique identifier), `description` (string),
  `status` ("pending" or "completed").

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users add a task and see it listed with id and pending status immediately after the
  command.
- **SC-002**: Users update or complete a task in one command and the next view reflects the change.
- **SC-003**: Error feedback clearly explains invalid input or missing ids, enabling users to recover
  without retries more than once.
- **SC-004**: All defined tests execute with 100% coverage and static type checks report zero errors,
  demonstrating conformance to quality gates.
