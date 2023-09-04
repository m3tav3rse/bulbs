import pytest
from mod import validator


def test_validate_type_valid():
    try:
        validator.validate_type(1.0, float)
    except TypeError:
        assert False

def test_validate_type_invalid_type():
    with pytest.raises(TypeError) as e:
        validator.validate_type(1, float)

def test_validate_range_valid():
    try:
        validator.validate_range(0.8, 0.0, 1.0)
    except ValueError:
        assert False

def test_validate_range_invalid_smaller():
    with pytest.raises(ValueError) as e:
        validator.validate_range(-0.1, 0.0, 1.0)

def test_validate_range_invalid_bigger():
    with pytest.raises(ValueError) as e:
        validator.validate_range(1.1, 0.0, 1.0)

def test_validate_hex_valid():
    try:
        validator.validate_hex("#09AF55")
    except ValueError:
        assert False

def test_validate_hex_invalid_type():
    with pytest.raises(TypeError) as e:
        validator.validate_hex(0x09AF55)

def test_validate_hex_invalid_length():
    with pytest.raises(ValueError) as e:
        validator.validate_hex("#09AF")

def test_validate_hex_invalid_hash():
    with pytest.raises(ValueError) as e:
        validator.validate_hex("09AF55")

def test_validate_hex_invalid_value():
    with pytest.raises(ValueError) as e:
        validator.validate_hex("#/:@G55")

