# Quickstart: Interactive CLI UX

## Prerequisites
- Python 3.12+
- `uv` installed

## Setup
```bash
cd /home/aie/all_data/piaic71-hackathon/hackathon2-sdd-b
uv pip install -r requirements.txt  # or uv pip install typer questionary rich pytest pytest-cov
```

## Run CLI (interactive defaults)
```bash
uv run python -m app.cli add
uv run python -m app.cli list
```

## Run CLI (flag-driven)
```bash
uv run python -m app.cli add --title "Write spec" --priority high --notes "first task"
uv run python -m app.cli list --priority high
```

## Tests and coverage
```bash
uv run pytest --cov=app --cov=tests --cov-report=term-missing
```

## Development tips
- Prefer interactive prompts for manual use; keep flag paths available for automation.
- Use Rich tables/panels for output; avoid raw prints.
- Keep error messages single-sentence with corrective action; no stack traces in user output.
