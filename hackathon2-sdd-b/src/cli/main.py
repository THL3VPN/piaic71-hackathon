"""CLI entry point."""
from .app import app


def run():  # pragma: no cover - wrapper
    app()


if __name__ == "__main__":  # pragma: no cover
    run()
