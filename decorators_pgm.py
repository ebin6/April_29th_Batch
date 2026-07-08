'''
def my_dec(fun):
    def wrapper():
        print("Hello from decorator")
        fun()
    return wrapper

@my_dec
def greet():
    print("Hello from greet")

greet()

'''
def myDec(fun):
    def wrapper(a,b):
        if b>0:
            fun(a,b)
        else:
            print("b must be grater than zero")
    return wrapper

@myDec
def divide(a,b):
    print(a/b)


divide(34,0)