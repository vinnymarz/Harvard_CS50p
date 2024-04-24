import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try: #reads input csv, writes to output csv - newline="" ensures correct line endings
        #outfile = open(sys.argv[2], "w", newline="")
        with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w", newline="") as outfile:
            reader = csv.DictReader(infile, fieldnames=["name", "house"])
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            #split last name, first name
            writer.writerows([{
                "first": first,
                "last": last,
                "house": row["house"]}
                for row in reader if "," in row["name"]
                for last, first in [row["name"].split(", ")]])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
