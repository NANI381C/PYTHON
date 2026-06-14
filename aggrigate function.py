class Charger:
    def __init__(self,name):# type: ignore
        self.cname=name
    def getCharger(self):
        print("Charger is Connected to Mobile")
class Mobile:
    def __init__(self,name):# type: ignore
        self.mname=name
        self.c=""
    def hasMobile(self,p): # type: ignore
        self.c=p # type: ignore
m1=Mobile("IQOO")
c1=Charger("C pin")
m1.hasMobile(c1) # type: ignore
print(m1.mname)
print(m1.c.cname) # type: ignore
m1.c.getCharger()# type: ignore
del m1   # type: ignore
print(c1.cname)
c1.getCharger()

