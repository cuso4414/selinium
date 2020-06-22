
def log2(func):
    def log():
        print("{} is running".format(func))
        func()
    return log

@log2
def foo2():
    print("this is a func, foo2")

foo2()