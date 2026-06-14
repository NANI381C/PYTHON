class person:
    def __init__(self):
        self.__name=""
    def setter(self,val): # type: ignore
        self.__name=val # type: ignore
    def getter(self): # type: ignore
        return self.__name # type: ignore
    getset=property(getter,setter) # type: ignore
p1=person()
p1.getset="Nasu"
res=p1.getset
print(res)
