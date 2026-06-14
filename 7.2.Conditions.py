a=int(input("Enter a num"))
b=int(input("Enter a num"))
c=int(input("Enter a num"))
if a>b>c:
    print("a is greater then all")
elif b>a>c:
    print("b is greater then all")
elif c>b>a:
    print("c is greater then all")   
else:
    print("a&b&c Both are equal")