from cli import errors


def test_format_error_defaults():
    assert errors.format_error("") == "Something went wrong. Please try again."


def test_format_error_strips():
    assert errors.format_error("  bad ") == "bad"
