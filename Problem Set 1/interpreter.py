expression = input("Enter an arithmetic expression: ").strip()

x, y, z = expression.split()

x = int(x)
z = int(z)

if int(x) and int(z) and y=="+":
    sum = float(x + z)
    print(f"{sum:.1f}")
elif int(x) and int(z) and y=="-":
    sum = float(x - z)
    print(f"{sum:.1f}")
elif int(x) and int(z) and y=="*":
    sum = float(x * z)
    print(f"{sum:.1f}")
elif int(x) and int(z) and y=="/":
    sum = float(x/z)
    print(f"{sum:.1f}")
