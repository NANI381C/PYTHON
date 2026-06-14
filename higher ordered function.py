#def fun1():
#    print("inside fun1")
#def fun2(ptr):
#    print("Entering fun2")
 #   ptr()
  #  print("Leaving fun2")
#fun1()
#fun2(fun1)
#output:
#inside fun1
#Entering fun2
#inside fun1    
#leaving fun2

a=10
def fun1():
    a=100
    b=200
    print(a)
    print(b)
def fun2():
    c=500
    print(a)
    print(c)
fun1()
fun2()

a=100
def fun1():
    global a
    a=10
    b=20
    print(a)
    print(b)
def fun2():
    global a
    a=15
    b=25
    print(a)
    print(b)
print(a)
fun1()
print(a)
fun2()
print(a)
