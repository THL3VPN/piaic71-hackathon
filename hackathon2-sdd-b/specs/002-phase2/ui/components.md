# Phase II UI Components

- **TaskList**
  - Props: `tasks`, `onComplete(taskId)`, `onEdit(taskId)`, `onDelete(taskId)`, `onPaginate(params)`.
  - Behavior: render empty state, loading, and error states; show status badges; action buttons call handlers.

- **TaskItem**
  - Props: `task`, `onEdit`, `onDelete`, `onComplete`.
  - Behavior: display title, description, completed badge; invoke handlers; disable actions during in-flight operations.

- **TaskForm**
  - Props: `initialTask?`, `mode` (create|edit), `onSubmit(payload)`, `onCancel`.
  - Fields: title (required, ≤200), description (optional, ≤2000).
  - Behavior: client-side validation; shows server errors; supports loading/disabled states.

- **Filters**
  - Props: `status`, `onChange({ status, sort, limit, offset })`.
  - Behavior: drive query params consistent with API (status, limit/offset, sort).
