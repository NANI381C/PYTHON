class Farmer:
    r=2.5
    def  __init__(self,p,t): # type: ignore
        self.principle=p
        self.time=t
    def loan(self):
        si=(self.principle*self.time*Farmer.r)/100 
        print(si) 
f1=Farmer(200000,4)
f2=Farmer(500000,7)
f1.loan()
f2.loan()
print(Farmer.r)
