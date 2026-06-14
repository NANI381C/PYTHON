class Hero:
    def __init__(self):
        self.name = "Prabhas"
        self.age = 40
        self.numOfMOvies = 24
    def act(self):
        print("Prabhas is a good actor.")
h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMOvies)
h1.act()