class Heart:
    def __init__(self):
        self.status="empty"
        print("Heart is pumping")
    def HeartAttack(self):
        print("The person is suffering from HeartAttack")
class cycle:
    def __init__(self,name):
        self.cname=name
    def buycycle(self):
        print("person buying a cycle")
class person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart()
        self.c=""
    def hasperson(self,p1):
        self.c1=p1
p1=person("Nani")
c1=cycle("hero")
p1.hasperson(c1)
print(p1.pname)
print(p1.h.status)
p1.h.HeartAttack()
print(p1.c1.cname)
p1.c1.buycycle()
del p1
print(c1.cname)
c1.buycycle()
print(p1.h1.status)
