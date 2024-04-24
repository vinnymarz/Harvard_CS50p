def main():
    coke_machine()

def coke_machine():

    total_paid = 0
    paid = 0
    due = 50

    while True:
        print("Amount Due:", due)
        n = int(input("Insert Coin:"))
        if n == 5 or n == 10 or n == 25:
            total_paid += n
            due -= n
            paid = n - due
        if due <= 0:
            change = total_paid - 50
            print("Change Owed:", change)
            break

main()
