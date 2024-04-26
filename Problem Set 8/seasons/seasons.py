from datetime import date
import inflect
import sys

def get_user_dob():
    while True:
        dob = input("Date of Birth: ")
        try:
            year, month, day = map(int, dob.split('-'))
            valid_date = date(year, month, day)
            return valid_date
        except:
            sys.exit(1)

def calculate_age_in_minutes(dob):
    today = date.today()
    difference = today - dob
    age_in_minutes = difference.total_seconds() // 60
    return round(age_in_minutes)

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number).replace(" and ", " ")

def main():
    dob = get_user_dob()
    age_in_minutes = calculate_age_in_minutes(dob)
    age_in_words = convert_to_words(age_in_minutes).capitalize()
    print(f"{age_in_words} minutes")

if __name__ == "__main__":
    main()
