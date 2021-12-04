import pytest

from scripts.display import Display


def test_display_init():
    display = Display()
    assert hasattr(display, "left_column_max")
    assert hasattr(display, "middle_column_max")
    assert hasattr(display, "right_column_max")
    assert hasattr(display, "init_rows")
    assert hasattr(display, "delim_1")
    assert hasattr(display, "delim_2")