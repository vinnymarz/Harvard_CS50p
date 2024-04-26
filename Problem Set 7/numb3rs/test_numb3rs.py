from numb3rs import validate
import pytest


def test_range():
    assert validate("234.233.232.231") == True
    assert validate("234.233.232.275") == False


def test_input():
    assert validate("234.233.232.cat") == False
    assert validate("234.233.232,275") == False
