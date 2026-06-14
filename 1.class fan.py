class fan:
    def __init__(self):
        self.brand="usha"
        self.color="white"
        self.cost=2500
        self.wings=3
    def on(self):
        print("Fan is ON")
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is OFF")
f1=fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.wings)
f1.on()
f1.rotate()
f1.off()