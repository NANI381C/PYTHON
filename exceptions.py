try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
    print(result)
except ValueError:
    print("it is value error")
except ZeroDivisionError:
    print("it is zero division error")
except Exception as e:
    print("it is an exception")