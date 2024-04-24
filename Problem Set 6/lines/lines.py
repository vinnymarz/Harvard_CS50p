import sys

def main():
    #if len(sys.argv) != 2:
        #sys.exit()
    if len(sys.argv)==2:
        filename = sys.argv[1]
        count = count_lines(filename)
        print(count)
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


def count_lines(filename):
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            return sum(1 for line in file if line.strip() and not line.lstrip().startswith('#'))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
