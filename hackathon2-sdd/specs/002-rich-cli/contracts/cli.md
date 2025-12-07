# CLI Contracts: Rich CLI Todo Experience

## Non-interactive commands
- `todo add --description "<text>"` → creates task, prints id/description/status.
- `todo view` → lists tasks in Rich table; empty state prints friendly message.
- `todo update --id <int> --description "<text>"` → updates description; prints updated info.
- `todo complete --id <int>` → marks completed; if already completed, prints informative message.
- `todo delete --id <int>` → deletes task; prints confirmation.
- Unknown commands or missing required args → print usage/help and exit non-zero.

## Interactive mode
- Entry command: `todo interactive` (or a `--interactive` flag) launches Questionary menu:
  - Choices: Add, View, Update, Complete, Delete, Exit/Cancel.
  - Prompts for required inputs; validation errors are shown immediately; successful operations reuse
    same output formatting as non-interactive commands (Rich tables/panels).

## Errors/Usage
- Empty description → “Description cannot be empty” on stderr/panel; exit code non-zero.
- Invalid/negative id → “Task id must be positive” or “Task <id> not found”; exit code non-zero.
- Missing required args → argparse-style usage plus friendly guidance.
- Unknown command → usage plus list of valid operations.
