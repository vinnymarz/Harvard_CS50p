import seasons
from datetime import date


def test_calculate_age_in_minutes():
    dob = date(1990, 1, 1)
    today = date.today()
    difference = today - dob
    expected_age_in_minutes = round(difference.total_seconds() // 60)
    assert seasons.calculate_age_in_minutes(dob) == expected_age_in_minutes

def test_convert_to_words():
    assert seasons.convert_to_words(0) == "zero"
    assert seasons.convert_to_words(10) == "ten"
    assert seasons.convert_to_words(100) == "one hundred"
    assert seasons. convert_to_words(123456) == "one hundred twenty-three thousand, four hundred fifty-six"
