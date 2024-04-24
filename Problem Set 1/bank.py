greeted = str(input("Please state a greeting: ")).lower().strip()

if greeted.startswith("hello"):
    print("$0")
elif greeted.startswith("h") and greeted != "hello":
    print("$20")
else:
    print("$100")
