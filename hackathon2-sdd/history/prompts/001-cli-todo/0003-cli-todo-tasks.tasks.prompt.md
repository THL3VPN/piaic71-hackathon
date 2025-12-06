---
id: 0003
title: cli-todo-tasks
stage: tasks
date: 2025-12-06
surface: codex-cli
model: gpt-5-codex
feature: 001-cli-todo
branch: 001-cli-todo
user: user
command: manual
labels: [tasks]
links:
  spec: hackathon2-sdd/specs/001-cli-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: hackathon2-sdd/specs/001-cli-todo/tasks.md
    summary: Task breakdown with TDD-first steps per story, dependencies, and review checkpoints.
tests:
  - status: not_run
    details: Task planning only; no automated tests executed.
---

## Prompt

Break plan into small tasks (T001..), each ≤ 3 minutes, testable, reversible. Add dependencies between tasks; group into phases; mark deliverables per task. Group tasks by operations and for each operation like add use TDD approach so RED Tests, Green Tests and Refactor. After each group we pause for human review and on approval commit to github. Focus on: - Use Context7 MCP server and pull documentations instead of assuming you know the best. - Use CLI commands where it;s more efficient than files manual creation. - TDD approach (tests first for each operation) - Small, step-by-step implementation - Clear task dependencies - Easy to undo changes

## Outline

1. **Setup**: Run `.specify/scripts/bash/check-prerequisites.sh --json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: Break plan into small tasks (T001..), each ≤ 3 minutes, testable, reversible. Add dependencies between tasks; group into phases; mark deliverables per task. Group tasks by operations and for each operation like add use TDD approach so RED Tests, Green Tests and Refactor. After each group we pause for human review and on approval commit to github. Focus on: - Use Context7 MCP server and pull documentations instead of assuming you know the best. - Use CLI commands where it;s more efficient than files manual creation. - TDD approach (tests first for each operation) - Small, step-by-step implementation - Clear task dependencies - Easy to undo changes

## Response snapshot

Created tasks.md with ≤3-minute TDD-first tasks per story (add/view, update/complete, delete), explicit dependencies, human review checkpoints, and paths under hackathon2-sdd/src and tests; noted MCP documentation lookup plan in research addendum.

## Outcome

- ✅ Impact: Tasks ready for execution with clear sequencing and review gates
- 🧪 Tests: Not run (task planning)
- 📁 Files: tasks.md added under feature directory
- 🔁 Next prompts: proceed to implementation following TDD and review checkpoints
- 🧠 Reflection: Common script root preference now stable; future tasks should fetch Context7 docs where available.

## Evaluation notes (flywheel)

- Failure modes observed: None during task generation
- Graders run and results (PASS/FAIL): Not run
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Automate MCP doc fetch step in tasks where supported.
