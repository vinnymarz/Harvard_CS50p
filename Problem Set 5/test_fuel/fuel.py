def main():
    z = input("Enter a fraction: ")
    percent = convert(z)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split(sep="/")
            x = int(x)
            y = int(y)
            z = x / y * 100
            if 100 >= z >= 0:
                return z
            if y == 0:
                raise ZeroDivisionError("Can't divide by zero")
            if x > y:
                print("Numerator must be less than or equal to denominator")
        except ValueError:
            print("Must be an integer")
        except ZeroDivisionError as e:
            print(e)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
