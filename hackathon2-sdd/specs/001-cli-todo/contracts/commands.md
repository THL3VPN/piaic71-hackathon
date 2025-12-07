# CLI Contracts: CLI Todo App

All commands are invoked via `python -m todo <command> [options]` (exact entrypoint to be finalized in
implementation) and operate on the in-memory store for the current session. Commands return human-
readable lines to stdout on success; errors go to stderr with non-zero exit codes.

## add
- **Input**: `--description "<text>"` (string, required; trimmed; must be non-empty).
- **Behavior**: Creates a new task with next id and `pending` status.
- **Success Output**: `Created task <id>: <description> [pending]`
- **Errors**:
  - Empty description → `Description cannot be empty` (exit 1)

## view
- **Input**: None.
- **Behavior**: Lists all tasks with `id`, `description`, `status` in insertion order.
- **Success Output**:
  - No tasks: `No tasks yet.`
  - With tasks: one line per task, e.g., `<id>: <description> [pending|completed]`
- **Errors**: None (treated as success with empty list message).

## update
- **Input**: `--id <int>` (required, must exist), `--description "<text>"` (required, trimmed, non-
  empty).
- **Behavior**: Updates description, retains status.
- **Success Output**: `Updated task <id>: <description> [<status>]`
- **Errors**:
  - Missing id → `Task id is required` (exit 1)
  - Unknown id → `Task <id> not found` (exit 1)
  - Empty description → `Description cannot be empty` (exit 1)

## complete
- **Input**: `--id <int>` (required, must exist).
- **Behavior**: Marks task status to `completed`; idempotent if already completed.
- **Success Output**:
  - Pending → `Completed task <id>: <description>`
  - Already completed → `Task <id> is already completed`
- **Errors**:
  - Missing id → `Task id is required` (exit 1)
  - Unknown id → `Task <id> not found` (exit 1)

## delete
- **Input**: `--id <int>` (required, must exist).
- **Behavior**: Removes task from store; ids are not reused.
- **Success Output**: `Deleted task <id>`
- **Errors**:
  - Missing id → `Task id is required` (exit 1)
  - Unknown id → `Task <id> not found` (exit 1)
