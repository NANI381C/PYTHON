try:
    a=int(input("enter a val"))
    b=int(input("enter a val"))
    res = a/b
    print(res)
except Exception as e:
    print("it is an exception:")
    print(e)
else:
    print("pgm run successfully")
