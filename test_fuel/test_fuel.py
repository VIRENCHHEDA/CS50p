from fuel import convert, gauge
import pytest


# test correct inputs
def test_correct_inputs():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

# test ZeroDivisionError
def test_zeroDivision_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# test ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")