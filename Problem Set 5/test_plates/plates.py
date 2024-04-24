def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:1].isdigit():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    first_num = True
    for i in s:
        if i == "0" and first_num == True:
            return False
        if i.isdigit():
            first_num = False
        if i.isalpha() and first_num ==  False:
            return False
        if not i.isalnum():
            return False

    return True

if __name__=="__main__":
    main()
