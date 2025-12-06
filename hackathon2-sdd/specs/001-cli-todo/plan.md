# Implementation Plan: CLI Todo App

**Branch**: `001-cli-todo` | **Date**: 2025-12-06 | **Spec**: hackathon2-sdd/specs/001-cli-todo/spec.md  
**Input**: Feature specification from `hackathon2-sdd/specs/001-cli-todo/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Deliver a command-line todo app that stores tasks in memory for the session. Users can add, view,
update descriptions, mark complete, and delete by id. All operations require string inputs, clear
docstrings, full type hints, and TDD with 100% test coverage and mypy passing per constitution.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: Standard library (`argparse` for CLI, `dataclasses`, `typing`)  
**Storage**: In-memory list/dict for tasks (no persistence)  
**Testing**: pytest + coverage; mypy for type checking  
**Target Platform**: POSIX-like shell (Linux/macOS); assumes standard Python runtime  
**Project Type**: single  
**Performance Goals**: Responsive CLI for small task lists (<10k items) with O(1) lookup by id  
**Constraints**: TDD sequence, 100% coverage, type-hinted functions, docstrings on all functions, use
dataclasses for task models, functional approach where reasonable, follow constitution rules  
**Scale/Scope**: Single CLI tool, no external services or persistence

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Tests first: plans must schedule pytest cases before implementation, with red-green-refactor flow
  and ≥80% line coverage targets documented.
- Runtime stack: Python 3.12+ only, type hints everywhere, and dataclasses for data models;
  dependencies managed with `uv` (lock and sync).
- Simplicity: proposed designs must demonstrate SOLID/DRY/KISS adherence and avoid unnecessary
  abstractions.
- Decision trail: any architecture/tooling/data-model choice that changes defaults requires an ADR in
  `history/adr/` before implementation work begins.
- Repository hygiene: all outputs are tracked in git; no untracked generators or manual system
  dependencies outside `uv`.

## Project Structure

### Documentation (this feature)

```text
hackathon2-sdd/specs/001-cli-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
hackathon2-sdd/src/
├── models/              # dataclasses for Task
├── services/            # pure functions handling task lifecycle
├── cli/                 # CLI entrypoints and parsing
└── lib/                 # shared helpers (formatting, validation)

hackathon2-sdd/tests/
├── unit/                # function-level tests (write first)
├── integration/         # end-to-end CLI command flows
└── contract/            # command-level contracts if needed
```

**Structure Decision**: Single-project layout under `hackathon2-sdd/` with `src` and `tests` mirroring
components. CLI uses `argparse`; services remain pure/functional over in-memory store.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| - | - | - |

**Post-design Constitution Check**: All gates satisfied (TDD-first flow, typed Python 3.12 with
dataclasses, uv-managed deps, no complexity exceptions).
