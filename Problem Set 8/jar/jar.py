def main():
    jar = Jar()
    while True:
        print(f"Jar: {jar}")
        print(f"Capacity: {jar.capacity}")
        action = input("Do you want to deposit or withdraw cookies, or are you just looking? ").lower().strip()
        if action == "deposit":
            n = int(input("How many cookies do you want to deposit? ")).strip()
            try:
                jar.deposit(n)
            except ValueError as e:
                print(e)
        elif action == "withdraw":
            n = int(input("How many cookies do you want to withdraw? ")).strip()
            try:
                jar.withdraw(n)
            except ValueError as e:
                print(e)
        elif action == "just looking":
            print("Don't look too long, they'll be gone before you know it!")
            break
        else:
            print("Please enter either 'deposit' , 'withdraw' , or 'just looking'.")


if __name__ == "__main__":
    main()
