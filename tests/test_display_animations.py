import pytest

from scripts.display import Display
from animations.animation import Animation


def test_display_init():
    display = Display()
    assert hasattr(display, "max_column_lengths")
    assert hasattr(display, "display")
    assert hasattr(display, "delim_1")
    assert hasattr(display, "delim_2")


def test_display_max_row_count():
    display = Display()
    assert type(display._get_max_row_count()) == int


def test_animations_init():
    anim = Animation()
    assert hasattr(anim, "frames")


def test_animation_getFrame():
    anim = Animation()
    assert type(anim.getFrame(0)) == list