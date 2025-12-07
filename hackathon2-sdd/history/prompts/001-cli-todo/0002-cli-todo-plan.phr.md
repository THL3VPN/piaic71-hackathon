---
id: 0002
title: cli-todo-plan
stage: plan
date: 2025-12-06
surface: codex-cli
model: gpt-5-codex
feature: 001-cli-todo
branch: 001-cli-todo
user: user
command: manual
labels: [plan]
links:
  spec: hackathon2-sdd/specs/001-cli-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: hackathon2-sdd/specs/001-cli-todo/plan.md
    summary: Implementation plan with technical context, gates, structure, and constitution re-check note.
  - path: hackathon2-sdd/specs/001-cli-todo/research.md
    summary: Decisions for CLI parsing, storage, task schema, error handling, IDs, and TDD quality gates.
  - path: hackathon2-sdd/specs/001-cli-todo/data-model.md
    summary: Task dataclass definition, validation rules, state transitions, and in-memory store structure.
  - path: hackathon2-sdd/specs/001-cli-todo/contracts/commands.md
    summary: CLI contracts for add/view/update/complete/delete commands with inputs, outputs, and errors.
  - path: hackathon2-sdd/specs/001-cli-todo/quickstart.md
    summary: Setup and TDD workflow with pytest/mypy commands and CLI usage examples.
  - path: hackathon2-sdd/AGENTS.md
    summary: Agent context updated with active technologies from plan.
tests:
  - status: not_run
    details: Planning artifacts only; no automated tests executed.
---

## Prompt

Create: architecture sketch, interfaces, data model, error handling, requirements. Decisions needing: list important choices with options and tradeoffs. Testing strategy: unit + integration tests based on acceptance criteria. Technical details: - Use a simple, functional approach where it makes sense - Use Python 3.12+ type hints with | union syntax - Follow TDD: write tests first, then implementation - Organize code and tests according to your constitution rules

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/setup-plan.sh --json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/bash/update-agent-context.sh codex`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

Created plan, research, data model, CLI command contracts, quickstart, and updated agent context for 001-cli-todo under hackathon2-sdd; gates satisfied with TDD/typed requirements; no clarifications pending.

## Outcome

- ✅ Impact: Planning artifacts ready for /sp.tasks with constitution gates satisfied
- 🧪 Tests: Not run (documentation phase)
- 📁 Files: Plan, research, data model, contracts, quickstart, agent context
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: Adjusted scripts to use project root when .specify lives under hackathon2-sdd.

## Evaluation notes (flywheel)

- Failure modes observed: setup-plan initial run targeted repo root specs; addressed by working within hackathon2-sdd paths and script root preference changes.
- Graders run and results (PASS/FAIL): Not run
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Improve create-phr path resolution similar to common.sh project root preference.
