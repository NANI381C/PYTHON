class student:
    def __init__(self):
        self.name="Nagasai"
        self.age=22
        self.usn=51
        self.gender="male"
    def study(self):
        print("Nagasai is NOT studying")
s1=student()
print(s1.name)
print(s1.age)
print(s1.usn)
print(s1.gender)
s1.study()