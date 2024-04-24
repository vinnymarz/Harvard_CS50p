def main():
    twitter = str(input("Input:")).strip()
    print(shorten(twitter))
    print()


def shorten(word):
    vowels = set("aeiouAEIOU")
    #vowels = ["a", "e", "i", "o", "u", "A," "E", "I", "O", "U"]
    shortened = ""
    for element in word:
        if element not in vowels:
           shortened += element
    return shortened


if __name__ == "__main__":
    main()
