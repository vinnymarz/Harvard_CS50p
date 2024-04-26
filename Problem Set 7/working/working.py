import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression pattern to match valid 12 hour time formats
    pattern = r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)"

    # Search for the pattern in the input
    if match := re.match(pattern, s):
        hour_start, minute_start, meridiem_start = int(match.group(1)), int(match.group(2) or 0), match.group(3)
        hour_end, minute_end, meridiem_end = int(match.group(4)), int(match.group(5) or 0), match.group(6)

        if minute_start == None:
            minute_start = 0
        if minute_end == None:
            minute_end = 0
        minute_start = int(minute_start)
        minute_end = int(minute_end)


        # Validate hour and minute
        if hour_start < 0 or hour_start > 12 or minute_start < 0 or minute_start >= 60:
            raise ValueError("Invalid start time")
        if hour_end < 0 or hour_end > 12 or minute_end < 0 or minute_end >= 60:
            raise ValueError("Invalid end time")

        # Convert to military time
        if meridiem_start == "PM" and hour_start != 12:
            hour_start += 12
            if hour_start == 24:
                hour_start = 0

        if meridiem_end == "PM" and hour_end != 12:
            hour_end += 12
            if hour_end == 24:
                hour_end = 0

        if meridiem_start == "AM" and hour_start == 12:
            hour_start = 0

        if meridiem_end == "AM" and hour_end == 12:
            hour_end = 0

        return f"{hour_start:02}:{minute_start:02} to {hour_end:02}:{minute_end:02}"
    else:
        raise ValueError("Invalid input")


if __name__ == "__main__":
    main()
