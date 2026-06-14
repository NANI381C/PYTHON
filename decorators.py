def main():
    str="pentagon"
    return str
def outer(ptr):
    print("inside inner")
    def inner():
        print("entering inner")
        res=ptr()
        ans=res.upper()
        print(ans)
        print("leaving inner")
    return inner
ref=outer(main)
ref()