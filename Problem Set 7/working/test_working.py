from working import convert
import pytest


def test_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:01 AM to 12:00 AM") == "09:01 to 00:00"

def test_errors():
    with pytest.raises(ValueError):
        convert("9 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("9 am - 5 am")
    with pytest.raises(ValueError):
        convert("9am to 5am")
