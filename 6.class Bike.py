class Bike:
    def __init__(self):
        self.brand = "RE"
        self.model = 1990
        self.color = "Black"
    def start(self):
        print("Bike is started")
        print(self.color)
        print(self)
b1 = Bike()
print(b1.brand)  
print(b1.model) 
print(b1.color) 
b1.start()
print(b1)    