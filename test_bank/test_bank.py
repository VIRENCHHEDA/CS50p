import bank
from bank import value

def test_return_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello hi") == 0

def test_return_20():
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("hi") == 20

def test_return_100():
    assert value("good morning") == 100
    assert value("namaskar") == 100