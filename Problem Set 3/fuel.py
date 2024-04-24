
#def get_fraction_percentage():
while True:
    try:
        x, y = input("Enter a fraction: ").split(sep="/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Can't divide by zero")
        z = x / y * 100
        if x > y:
            print("Numerator must be less than or equal to denominator")
        elif z <= 1:
            print("E")
            break
        elif z >= 99:
            print('F')
            break
        else:
            print(f'{z:.0f}%')
            break
    except ValueError:
        print("Must be an integer")
    except ZeroDivisionError as e:
            print(e)
