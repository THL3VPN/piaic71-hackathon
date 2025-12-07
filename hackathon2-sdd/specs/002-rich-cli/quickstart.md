# Quickstart: Rich CLI Todo Experience

## Prerequisites
- Python 3.13+
- `uv` installed

## Setup
```bash
cd /home/aie/all_data/piaic71-hackathon/hackathon2-sdd
uv sync
```

## Running Commands
```bash
uv run python -m todo add --description "Buy milk"
uv run python -m todo view
uv run python -m todo update --id 1 --description "Buy oat milk"
uv run python -m todo complete --id 1
uv run python -m todo delete --id 1
```

## Interactive Mode
```bash
uv run python -m todo interactive
# choose operation via Questionary prompts; outputs render with Rich
```

## TDD & Quality
```bash
PYTHONPATH=src uv run pytest --cov=src --cov=tests --cov-report=term-missing
PYTHONPATH=src uv run mypy src
```
