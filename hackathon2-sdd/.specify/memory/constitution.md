<!--
Sync Impact Report
- Version: UNSET -> 1.0.0
- Modified principles: Initial set established
- Added sections: Core Principles, Technical Stack & Quality Gates, Development Workflow & Review, Governance
- Removed sections: None
- Templates requiring updates: ✅ .specify/templates/plan-template.md; ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Hackathon2 SDD Constitution

## Core Principles

### I. Test-First Delivery (Non-Negotiable)
Tests drive all changes. Write pytest cases before code, run them to fail, then implement in a
red-green-refactor cycle. All merges require a green suite with at least 80% line coverage and no
unexplained reductions. Production code must not be written without a failing test that defines the
behavior.

### II. Modern Typed Python 3.12
Use Python 3.12+ exclusively. Apply type hints everywhere and treat type checking as a gate for
acceptance. Model data with `dataclass` (or compatible `dataclasses.dataclass`) by default to keep
schemas explicit and immutable where appropriate. Manage dependencies with `uv`; lock and sync
environments before sharing work.

### III. Simple, Readable OOP
Designs honor SOLID, DRY, and KISS. Prefer small, focused classes and functions with clear names and
docstrings where clarity is needed. Avoid needless abstractions and duplication; favor straightforward
composition over inheritance unless a stable contract exists.

### IV. Decision Traceability with ADRs
Record significant decisions (architecture, data models, tool changes, deviations from defaults) as
ADRs before implementation. Each ADR states context, options, trade-offs, and consequences. Store
them in `history/adr/` and link them from specs/plans; work blocked until required ADRs exist.

### V. Repository Discipline & Quality Gates
Git is the single source of truth: track all project files and generated artifacts that influence
builds or tests. Commits and PRs must include passing pytest runs that meet coverage targets. Manage
dependencies only through `uv` commands and commit lockfiles to keep environments reproducible.

## Technical Stack & Quality Gates

- Language: Python 3.12+ with comprehensive type hints; dataclasses are the default data structure.
- Package manager: `uv` for dependency resolution and locking; lockfiles are version-controlled.
- Testing: pytest is the standard runner; maintain ≥80% line coverage and raise thresholds when
  feasible. Tests are written first and must fail before implementation.
- Version control: All assets live in git; no manual changes outside tracked history.

## Development Workflow & Review

- Follow red-green-refactor: draft tests, watch them fail, implement minimal code, then refactor with
  coverage intact.
- Code reviews verify adherence to principles, especially TDD sequencing, typing completeness,
  dataclass usage for data models, and SOLID/DRY/KISS alignment.
- Require ADRs before merging work that alters architecture, data contracts, tooling, or quality bars
  to ensure decisions are durable and discoverable.
- Plans and tasks must schedule test creation ahead of implementation and call out coverage targets
  and type-check expectations.

## Governance

- This constitution supersedes other practices for this repository. Amendments require an ADR
  describing the change, impact, and migration plan, plus reviewer approval in git history.
- Versioning follows semantic rules: MAJOR for removals or incompatible redefinitions; MINOR for new
  principles or materially expanded guidance; PATCH for clarifications or typo-level edits.
- Compliance: Every PR reviewer must confirm principles are met, tests are green with required
  coverage, type checks pass, and ADRs are linked where applicable. Periodic audits ensure no drift
  from the TDD, typing, and git discipline requirements.

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
