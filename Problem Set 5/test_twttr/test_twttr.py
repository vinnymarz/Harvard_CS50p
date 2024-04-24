from twttr import shorten
import pytest

def test_short():
    assert shorten("David") == "Dvd"
    assert shorten("david") == "dvd"
    assert shorten("Mr. Martin, won't you please join me?") == "Mr. Mrtn, wn't y pls jn m?"

def test_vow():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_str():
    with pytest.raises(TypeError):
        shorten(int)
        shorten(float)
        shorten(bool)

def test_int():
     assert shorten("1234567890") == "1234567890"
