class mobile:
    def __init__(self):
        self.brand = "Apple"
        self.model = "iPhone 17 Pro"
    def call(self):
        print("The mobile is calling.")

    @staticmethod
    def charge():
        print("The mobile is charging.")

    @classmethod
    def hang(cls):
        print("The mobile is hanging.")
m1 = mobile()
print(m1.brand)
print(m1.model)
m1.call()
mobile.charge()
mobile.hang()