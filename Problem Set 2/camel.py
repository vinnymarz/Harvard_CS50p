camelCase = input("camelCase:").strip()

for c in camelCase:
    if c.isupper():
        c = c.lower()
        print("_", sep="", end="")
    print(c, sep="", end="")
print()
