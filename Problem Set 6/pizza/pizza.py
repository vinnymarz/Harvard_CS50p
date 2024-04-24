from tabulate import tabulate
import sys
import csv

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")

try:
    with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            menu = list(reader)
            print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))
except FileNotFoundError:
     sys.exit("File does not exist")
