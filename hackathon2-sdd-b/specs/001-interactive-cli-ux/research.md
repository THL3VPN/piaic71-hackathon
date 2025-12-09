# Research: Interactive CLI UX

## Decisions and Findings

### Typer for CLI command structure
- **Decision**: Use Typer to define commands/subcommands for add/list/delete and share option parsing between interactive and flag-driven modes.
- **Rationale**: Typer provides intuitive parameter typing, help text, and testing hooks via runner utilities; aligns with spec requirement for clean commands.
- **Alternatives considered**: Click (heavier boilerplate, Typer built atop it), argparse (minimal but lacks interactive ergonomics).

### Questionary for interactive prompts
- **Decision**: Use Questionary prompts (text, select, confirm) for interactive flows; keep a thin wrapper to allow reuse in tests and flag-driven paths.
- **Rationale**: Matches requirement for menus; wrappers enable mocking prompts for pytest without patching global input repeatedly.
- **Alternatives considered**: InquirerPy (similar but adds dependency overhead), raw `input()` (harder to style/test).

### Rich for output formatting
- **Decision**: Render task lists as Rich tables with consistent columns (title, priority, status, due date, notes) and use colored text for success/error.
- **Rationale**: Rich tables improve scanability; color helpers allow readable fallbacks when color is unsupported.
- **Alternatives considered**: Plain print/tty tables (reduced clarity), Textual (too heavy for current scope).

### Dual-mode interaction (prompts + flags)
- **Decision**: All commands accept flags for automation while defaulting to prompts when flags are missing; destructive actions require confirmation prompts.
- **Rationale**: Meets spec for interactive defaults and automation support; confirmation reduces accidental deletes.
- **Alternatives considered**: Prompt-only (blocks automation), flag-only (hurts usability for new users).

### Error handling and messaging
- **Decision**: Centralize error formatting to emit single-sentence guidance plus corrective action; avoid stack traces in user output.
- **Rationale**: Satisfies friendly error requirement and keeps messaging consistent; stack traces reserved for logs/tests.
- **Alternatives considered**: Per-command errors (inconsistent), raising raw exceptions (leaks internals).

### Testing strategy and coverage
- **Decision**: Use pytest with coverage, exercising both interactive (mocked Questionary) and flag-driven flows; enforce ≥80% coverage with targeted contract/integration tests for commands and output rendering.
- **Rationale**: Aligns constitution quality gates and feature requirement; mocks keep tests fast and deterministic.
- **Alternatives considered**: Snapshot-only tests (miss logic), manual ad-hoc testing (insufficient for coverage gate).

### Color fallback and accessibility
- **Decision**: Detect color support via Rich console; degrade to plain text while preserving readable spacing; avoid color-only cues for status.
- **Rationale**: Ensures legibility in monochrome terminals and CI logs.
- **Alternatives considered**: Hard-coded colors (poor accessibility), disabling Rich styles entirely (loss of clarity).
