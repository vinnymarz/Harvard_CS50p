import random
import sys

def get_valid_input(prompt, lower_limit):
    while True:
        try:
            value = int(input(prompt))
            if value >= lower_limit:
                return value
        except ValueError:
            continue

def main():
    n = get_valid_input("Level: ", 1)
    number = random.randint(1, n)

    while True:
        try:
            guess = get_valid_input("Guess: ", 1)
            if guess == number:
                sys.exit("Just right!")
            elif guess < number:
                print("Too small!")
            else:
                print("Too large!")
        except EOFError:
            break

if __name__ == "__main__":
    main()
