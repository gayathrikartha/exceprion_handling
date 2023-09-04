
try:
    a = int(input("enter the number"))
    print(a)
except ValueError:
    raise ValueError("invalid literal")
finally:
    print("hi")
