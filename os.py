class Os:
    def __init__(self):
        self.status=True
        print("Os is Ready")
    def getOs(self):
        print("Os is installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.O=Os()
        print("Mobile is Ready")
        print("with Os Installed")
m1=Mobile("Nokia")
print(m1.mname)
print(m1.O.status)
print(m1.O.getOs())
del m1
print(m1.O.status)