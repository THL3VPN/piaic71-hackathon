# Data Model: CLI Todo App

## Entities

### Task
- **Fields**:
  - `id: int` — unique, monotonically increasing per session; assigned on add.
  - `description: str` — required, trimmed, must be non-empty after trimming.
  - `status: Literal["pending", "completed"]` — default `pending`; set to `completed` when marked.
- **Validation Rules**:
  - Reject empty/whitespace-only descriptions.
  - Status only accepts `pending` or `completed`.
  - Id must be positive integer and exist for update/complete/delete operations.
- **State Transitions**:
  - `pending` → `completed` (mark complete).
  - `completed` → `completed` (idempotent; no change but report already complete).

### InMemoryTaskStore (structural container)
- **Fields**:
  - `tasks: list[Task]` — ordered collection preserving insertion order.
  - `next_id: int` — counter starting at 1; increments on each add; not decremented on delete.
- **Behavior**:
  - Lookups by id are O(1) via helper index or O(n) scan; tests cover correctness, not perf extremes.
  - Deletes remove the task; ids are not reused.
