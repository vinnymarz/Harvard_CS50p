from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False


def test_plate_len():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_invalid_char():
    assert is_valid("PI3.14") == False


def test_leading_int():
    assert is_valid("12CS05") == False
    assert is_valid("0CS50P") == False


def test_non_alpha():
    assert is_valid("123456") == False
