import sys
import pytest

sys.path.append("mod")

import converter

def test_rgb_to_hex():
    assert converter.rgb_to_hex((21, 37, 0)) == "#152500"

def test_hex_to_rgb():
    assert converter.hex_to_rgb("#152500") == (21, 37, 0)
