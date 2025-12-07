from __future__ import annotations

import pytest

from services import store


def test_update_task_missing_id_raises():
    with pytest.raises(ValueError):
        store.update_task(99, "desc")


def test_complete_task_missing_id_raises():
    with pytest.raises(ValueError):
        store.complete_task(42)


def test_delete_task_missing_id_raises():
    with pytest.raises(ValueError):
        store.delete_task(7)


def test_require_id_positive():
    with pytest.raises(ValueError):
        store.complete_task(0)


def test_require_id_none():
    with pytest.raises(ValueError):
        store.delete_task(None)  # type: ignore[arg-type]
