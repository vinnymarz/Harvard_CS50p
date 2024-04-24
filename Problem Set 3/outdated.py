date = input("Enter a date (MM/DD/YYY or Month Day, Year): ").strip().lower()

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]


while True:
    try:
        # Date is in MM/DD/YYYY format
        if date[0].isdigit():
            month, day, year = date.split("/")
            month, day = int(month), int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        # Date is in Month day, year format
        else:
            month, day, year = date.split(" ")
            #day = day.rstrip(",")  # Remove any trailing comma
            x = len(day)-1
            day = day[0:x]
            day, month = int(day), months.index(month) + 1
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break


    except KeyError:
        continue
    except ValueError:
        pass
