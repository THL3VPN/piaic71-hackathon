# Data Model: Interactive CLI UX

## Entities

### Task
- **Fields**:
  - `id`: unique identifier (string/UUID provided by underlying storage)
  - `title`: required short text (1-120 chars)
  - `priority`: enum {low, medium, high}
  - `status`: enum {pending, done}
  - `due_date`: optional date
  - `notes`: optional free text (<= 500 chars)
- **Validation**:
  - title required; trim whitespace
  - priority must be one of allowed values
  - status defaults to `pending` when omitted
  - due_date, if provided, must be a valid date string
- **Relationships**: none (single-user scope)
- **State transitions**: status can move pending → done; reversible to pending via edit.

### CLI Session (interaction wrapper)
- **Fields**:
  - `mode`: {interactive, flags}
  - `io`: prompt/output adapters (Questionary for input, Rich for output)
- **Validation**: mode selection based on presence of flags; must support non-interactive environments.
- **Purpose**: encapsulate how commands gather input and render output while keeping business logic separate.
