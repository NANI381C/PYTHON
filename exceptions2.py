try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
    print(result)
except (ValueError, ZeroDivisionError) as e:
    print("it is value error or zero division error:", e)
except Exception as e:
    print("it is an exception:", e)