# CLI Command Contracts: Interactive CLI UX

## add
- **Purpose**: Create a task with title, priority, optional notes (and optional due date if available).
- **Invocation**:
  - Interactive default: `uv run python -m app.cli add`
  - Flags: `uv run python -m app.cli add --title "Write spec" --priority high [--notes "..." --due-date 2025-12-15]`
- **Prompts** (when flags missing):
  - title (text)
  - priority (select: low/medium/high)
  - notes (optional text)
  - confirm create (confirm)
- **Success Output**: Rich panel/colored line summarizing created task (id, title, priority, status=pending).
- **Errors**: Invalid priority or missing title returns single-sentence error plus hint to retry; no stack trace to user.

## list
- **Purpose**: Display tasks with optional filters.
- **Invocation**:
  - Interactive default: `uv run python -m app.cli list`
  - Flags: `uv run python -m app.cli list --priority high --status pending`
- **Prompts** (when flags missing):
  - filter by priority (select + "All")
  - filter by status (select + "All")
- **Output**: Rich table with columns: title, priority, status, due date, notes (truncated). Empty state shows friendly message.
- **Errors**: Bad filter values produce corrective message and re-prompt.

## view
- **Purpose**: Show details for a single task.
- **Invocation**: `uv run python -m app.cli view --id <task-id>`
- **Prompts**: If id not provided, present select list of tasks (title + status) to choose.
- **Output**: Rich panel with all task fields.
- **Errors**: Unknown id -> concise error with suggestion to list tasks first.

## delete
- **Purpose**: Remove a task.
- **Invocation**: `uv run python -m app.cli delete --id <task-id>`
- **Prompts**: If id missing, select task; always confirm deletion (confirm prompt).
- **Output**: Success line confirming deletion.
- **Errors**: Unknown id -> friendly guidance; cancel leaves data unchanged.

## common rules
- Commands must accept flags for automation while supporting interactive prompts by default.
- Destructive actions require confirmation.
- All outputs use Rich formatting with color-safe fallback.
- Errors are user-friendly and single-sentence with a corrective next step.
