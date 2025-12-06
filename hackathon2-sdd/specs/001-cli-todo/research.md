# Research: CLI Todo App

## Decisions

- **Decision**: Use `argparse` for CLI parsing with subcommands (`add`, `view`, `update`, `complete`,
  `delete`).  
  **Rationale**: Standard library, no extra deps, straightforward to test and document.  
  **Alternatives considered**: Click/Typer (richer UX, adds deps); manual `sys.argv` parsing (less
  robust).

- **Decision**: Store tasks in an in-memory list keyed by incremental integer id; expose pure
  functions that accept/return structures rather than mutate globals.  
  **Rationale**: Aligns with functional style and simplicity; easy to unit test; meets “in-memory”
  requirement.  
  **Alternatives considered**: Dict keyed by id only (fast lookups but requires extra ordering logic);
  class-based store (more structure, less functional).

- **Decision**: Represent tasks as a `dataclass` with fields `id: int`, `description: str`,
  `status: Literal["pending", "completed"]`.  
  **Rationale**: Dataclasses keep schema explicit with typing; literals enforce status domain.  
  **Alternatives considered**: Enum for status (more ceremony); plain dict (loses type guarantees).

- **Decision**: Error handling returns structured results per command: success flag, message,
  optional task payload; CLI prints human-readable messages and uses exit code 0 for success,
  non-zero for failures.  
  **Rationale**: Keeps CLI predictable and testable; aligns with acceptance criteria on formatting and
  correct results.  
  **Alternatives considered**: Exceptions bubbling to CLI (harder to test outputs); silent failures
  (unacceptable).

- **Decision**: ID generation uses monotonic counter scoped to the in-memory session; delete does not
  reuse ids.  
  **Rationale**: Simpler reasoning and avoids collisions; deterministic for tests.  
  **Alternatives considered**: Reuse deleted ids (can confuse users/tests); UUIDs (overkill for CLI).

- **Decision**: TDD workflow with pytest and mypy; target 100% coverage per acceptance criteria.  
  **Rationale**: Matches constitution and feature requirements; ensures confidence in CLI behaviors.  
  **Alternatives considered**: Lower coverage thresholds (contradicts requirements).

- **Decision**: Use Context7 MCP server for authoritative documentation lookups before choosing CLI
  patterns or libraries; prefer MCP-sourced guidance over assumptions.  
  **Rationale**: Reduces guesswork and aligns with environment-provided docs.  
  **Alternatives considered**: Relying on personal defaults (risk of mismatch); external web search
  (may be blocked).
