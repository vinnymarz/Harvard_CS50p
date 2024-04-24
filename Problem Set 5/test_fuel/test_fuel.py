from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/1")
