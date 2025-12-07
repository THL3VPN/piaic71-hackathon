# Data Model: Rich CLI Todo Experience

## Entities

### Task
- **Fields**:
  - `id: int` — unique, monotonically increasing per session.
  - `description: str` — required, trimmed, non-empty.
  - `status: Literal["pending", "completed"]` — default pending; completed when marked.
- **Validation Rules**:
  - Reject empty/whitespace-only descriptions.
  - Id must be positive integer and exist for operations.
- **State Transitions**:
  - `pending` → `completed`; `completed` → `completed` (idempotent).

### CLI Session (conceptual)
- Captures command args or interactive selections and maps to service calls; no persisted state beyond
  current process.
