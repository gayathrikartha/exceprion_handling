def oddeven(a):
    if (a % 2 == 0):
        print("even")
    else:
        print("odd")
try:
    a = int(input("enter the number"))
    oddeven(a)
except ValueError:
    raise ValueError("invalid error")
finally:
    print("sucess")