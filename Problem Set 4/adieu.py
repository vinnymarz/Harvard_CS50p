import inflect


def main():
    p = inflect.engine()
    name_list = get_names()
    my_list = p.join(name_list)
    print(f"Adieu, adieu, to {my_list}")


def get_names():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    return name_list


if __name__ == "__main__":
    main()
