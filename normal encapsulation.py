class person:
    def __init__(self):
        self.__name=""
    def setter(self,val):
        self.__name=val
    def getter(self):
        return self.__name
p1=person()
p1.setter("Nasu")
res=p1.getter()
print(res)