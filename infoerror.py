def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("entering occured in fun1")
        print("Learning fun1")
def fun2():
    print("entering fun2")
    res= 1 % Error
    print(res)
    print("learning fun2")
print("pg started")
fun1()
print("pg ended")