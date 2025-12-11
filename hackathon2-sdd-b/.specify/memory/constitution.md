<!--
Sync Impact Report
- Version: 1.0.0 → 1.1.0
- Modified principles: Spec-Driven Five-Phase Delivery (explicit SpecKit+ artifacts), Reviewable & Traceable Work (clarified PHR linkage)
- Added sections: VI. Terminal UX & Accessibility; CLI stack constraint in Technical Requirements
- Removed sections: none
- Templates requiring updates: .specify/templates/plan-template.md ✅ reviewed (aligned); .specify/templates/spec-template.md ✅ reviewed (aligned); .specify/templates/tasks-template.md ✅ reviewed (aligned); .specify/templates/commands/*.md ✅ reviewed (no agent-specific issues found)
- Follow-up TODOs: none
-->
# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Five-Phase Delivery (NON-NEGOTIABLE)
Every change moves through five written phases: Research, Specification, Design & Contracts, Implementation, and Validation & Release. Each phase must produce an artifact (research notes, spec, design/contracts, code with tests, validation report) that can be reviewed independently before advancing. SpecKit+ templates and commands must be used to generate and store artifacts. No phase may be skipped or merged without a documented amendment.

### II. Test Discipline & Coverage
Tests are authored before or alongside implementation using pytest. All tests must pass at all times. Coverage must remain at or above 80% for new and changed code, measured via pytest + coverage, with gaps explicitly justified. Gate builds on failing tests or coverage regressions.

### III. Python 3.12 + uv Reproducibility
Python 3.12+ is the only supported runtime. Dependency management uses `uv` with locked versions; no alternative package managers are permitted. All commands in plans, specs, and tasks must use `uv run`/`uv pip` to ensure reproducible environments across local and CI.

### IV. Incremental Value per Phase
Each phase must deliver a user-visible or testable increment tied to the phase goal (e.g., validated spec, signed-off contracts, running slice of functionality). Work items remain small enough to complete within a single phase cycle and keep dependency risk low.

### V. Reviewable & Traceable Work
Plans, specs, tasks, and code changes must reference each other so reviewers can trace decisions to artifacts. Every change must be reviewable asynchronously with clear acceptance criteria, test evidence, coverage data, and a Prompt History Record (PHR) captured before merge.

### VI. Terminal UX & Accessibility
All CLI interactions must prioritize readability and ease: Typer for commands, Questionary for choices/inputs, and Rich for tables and colored messages. Screens must provide breathable spacing, clear labels, and a Back/escape path for any interactive step. Errors stay simple and action-oriented. This keeps the interactive experience consistent and comfortable for every user.

## Technical Constraints & Quality Requirements
- Language: Python 3.12+ only.
- Package manager: `uv` with locked dependencies tracked in VCS.
- Testing: pytest with coverage reporting; failing or missing tests block merges.
- Quality thresholds: all tests green at all times; ≥80% coverage on new/changed code with rationale for any exception.
- CLI stack: Typer for commands, Questionary for interactive selections, Rich for output styling; keep outputs readable with spacing, headings, and Back/escape options.
- Tooling commands in docs and tasks must use `uv run` to ensure consistency across environments.

## Development Workflow & Phases
1. **Research**: Capture problem context, risks, and success measures.
2. **Specification**: Write a clear, testable spec informed by research.
3. **Design & Contracts**: Define data models, contracts, and plan structure aligned to the spec; exit requires review.
4. **Implementation**: Build to spec with tests-first, keeping changes scoped to planned increments.
5. **Validation & Release**: Run pytest with coverage, document results, and capture user-facing validation before release.

Phase transitions require explicit acceptance of the prior phase artifact. Work that cannot fit a single phase must be split before starting Implementation.

## Governance
- This constitution supersedes other process documents. All plans/specs/tasks must cite the relevant principles and note any exceptions with justification.
- Amendments require: a documented proposal, impact analysis, version bump per semantic versioning (MAJOR for principle removal/redefinition, MINOR for new/expanded principles, PATCH for clarifications), and reviewer approval.
- Compliance checks: every PR must state phase, artifacts produced, pytest results, coverage numbers, and link to the relevant PHR. Deviations must include time-bound remediation tasks.
- Runtime guidance (e.g., quickstart or agent guides) must stay in sync with principles and constraints in this document.

**Version**: 1.1.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10
