def add(x, y):
    return x+y
def multiply(x, y):
    return x * y

a = add(10, 15)

def newfunc(n):
    def myfunc(x):
        return n+x
    return myfunc
new = newfunc(100)
new(200) 