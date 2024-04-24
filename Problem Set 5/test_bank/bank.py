def main():
    greeting = input("Please state a greeting: ").lower().strip()
    #print(value(greeting))
    output = value(greeting)
    print(f"${output}")


def value(greeting):
    if greeting.startswith("hello"):
        #greeting = "0"
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        #greeting = "20"
        return 20
    else:
        #greeting = "100"
        return 100


if __name__ == "__main__":
    main()
