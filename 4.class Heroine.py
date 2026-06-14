class Heroine:
    def __init__(self):
        self.name="Rukku"
        self.age=27
        self.numOfMovies=7
    def act(self):
        print("Rukku is acting in a movie.")
h1=Heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.age=28#modifying existing attribute
print(h1.age)
del h1.numOfMovies#deleting existing attribute
#print(h1.numOfMovies)#this will give error as attribute is deleted