import random
#import sys


def main():
    score = 0
    attempts = 0
    incorrect_attempts = 0
    level = get_level()
    while attempts != 10:
        if incorrect_attempts == 0:
            x = generate_integer(level)
            y = generate_integer(level)
            answer = x + y
        try:
            user_answer = int(input(f"{x} + {y} = "))

            if user_answer == answer:
                attempts += 1
                score += 1
                incorrect_attempts = 0
                continue
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            incorrect_attempts += 1
            pass

        if incorrect_attempts == 3:
            #print(f"Score: {score}")
            #sys.exit()
            print(f"{x} + {y} = {answer}")
            incorrect_attempts = 0
            attempts += 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level

        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
