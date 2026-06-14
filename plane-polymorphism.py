class plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
class passenger(plane):
    def land(self):
        print("plane is landind")
class cargo(plane):
    def land(self):
        print("plane is landind")
class fighter(plane):
    def land(self):
        print("plane is landind")
p1=passenger()
c1=cargo()
f1=fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)