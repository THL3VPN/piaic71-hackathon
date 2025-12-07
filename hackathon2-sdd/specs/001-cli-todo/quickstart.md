# Quickstart: CLI Todo App

## Prerequisites
- Python 3.13+
- `uv` installed for dependency management

## Setup
```bash
cd /home/aie/all_data/piaic71-hackathon/hackathon2-sdd
uv sync
```

## TDD Workflow
1. Add/adjust tests first in `tests/unit/` or `tests/integration/`.
2. Run tests to see them fail: `uv run pytest`.
3. Implement minimal code in `src/`.
4. Re-run tests until green; keep coverage at 100% (per acceptance criteria).
5. Run type checks: `uv run mypy src`.

## Running the CLI (after implementation)
```bash
uv run python -m todo <command> [options]
# examples (subject to implementation names)
uv run python -m todo add --description "Buy milk"
uv run python -m todo view
uv run python -m todo update --id 1 --description "Buy oat milk"
uv run python -m todo complete --id 1
uv run python -m todo delete --id 1
# sample output
# Created task 1: Buy milk [pending]
# 1: Buy milk [pending]
# Updated task 1: Buy oat milk [pending]
# Completed task 1: Buy oat milk
# Deleted task 1
uv run python -m todo update --id 1 --description "Buy oat milk"
uv run python -m todo complete --id 1
uv run python -m todo delete --id 1
```

## Test Commands
```bash
uv run pytest --cov=src --cov=tests --cov-report=term-missing
uv run mypy src
```
