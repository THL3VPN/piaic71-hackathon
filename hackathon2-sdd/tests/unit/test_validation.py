from __future__ import annotations

import pytest

from lib import validation


def test_parse_task_id_accepts_positive_int_string() -> None:
    assert validation.parse_task_id("5") == 5
    assert validation.parse_task_id(" 7 ") == 7
    assert validation.parse_task_id(3) == 3


@pytest.mark.parametrize("raw", ["0", "-1", "", "abc", None, -2, 0])
def test_parse_task_id_rejects_invalid_input(raw: object) -> None:
    with pytest.raises(ValueError):
        validation.parse_task_id(raw)  # type: ignore[arg-type]


def test_require_description_trims_and_validates() -> None:
    assert validation.require_description("  test  ") == "test"
    with pytest.raises(ValueError):
        validation.require_description("   ")
