import re
import sys

def main():
    print(count(input("Input: ")))

def count(s):
    # Use regular expression to find whole word 'um' case-insensitively
    #\b on either side ensures only matching um as a whole word
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
