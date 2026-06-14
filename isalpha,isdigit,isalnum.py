str=input("enter a string")
print(str)
if str.isalpha():
    print("str contains only Alpha")
elif str.isdigit():
    print("contains only digits")
elif str.isalnum():
    print("contains both")
else:
    print("other char")

