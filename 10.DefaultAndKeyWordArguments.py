class demo:
    def dis(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
d1=demo()
x=11
y=22
z=33
d1.dis()
d1.dis(x,y,z)
d1.dis(x)
d1.dis(z)
d1.dis(y,z)
d1.dis(b=z,a=y,c=x)
d1.dis(c=y)
