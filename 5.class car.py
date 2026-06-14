class car:
    def __init__(self):
        self.name = "Rolls Royce"
        self.color = "Black"
        self.year = 2020
    def drive(self):
        print("The car is driving smoothly.")
    def speed(self):
        print("The car is going 120 km/h.")
c1=car()
print(c1.name)
print(c1.color)
print(c1.year)
c1.drive()
c1.speed()
c1.year=2022
c1.color="White"
print(c1.color)