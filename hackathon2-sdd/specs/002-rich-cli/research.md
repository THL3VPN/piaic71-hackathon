# Research: Rich CLI Todo Experience

## Decisions

- **Decision**: Use argparse for base CLI parsing with subcommands for add/view/update/complete/delete.  
  **Rationale**: Standard library, low dependency footprint, aligns with prior CLI.  
  **Alternatives considered**: Click/Typer (higher dependency/weight), manual parsing (error-prone).

- **Decision**: Use Questionary for interactive mode to select operations and gather inputs.  
  **Rationale**: Meets interactive requirement; supports lists and prompts with minimal boilerplate.  
  **Alternatives considered**: InquirerPy (similar but extra dependency), custom menus (less UX).

- **Decision**: Use Rich for output formatting (tables/panels) and degrade gracefully to plain text.  
  **Rationale**: Meets “good output” constraint without Streamlit; widely used, readable defaults.  
  **Alternatives considered**: Plain print (worse UX), Streamlit (not suitable for CLI).

- **Decision**: Preserve in-memory store; no external persistence.  
  **Rationale**: Matches existing app; keeps CLI fast and simple.  
  **Alternatives considered**: File/DB persistence (out of scope for this feature).

- **Decision**: Error handling uses structured validation with Rich-styled error panels; exits non-zero
  on failures; usage/help shown for unknown/missing args.  
  **Rationale**: Aligns with acceptance criteria and constitution on clarity.  
  **Alternatives considered**: Silent failures or generic errors (unacceptable).

- **Decision**: TDD with pytest + coverage 100% and mypy strict; Python 3.13.  
  **Rationale**: Constitution compliance.  
  **Alternatives considered**: Lower coverage or relaxed typing (rejected).
