'''
写一个简单的例子，没有返回值，只打印一句“这是一个函数”
增加需求，记录下函数的执行日志，在代码中添加日志代码
重新定义一个函数：专门处理日志，日志处理完之后再执行真正的业务代码
'''

def foo():
    print("this is a func,foo")
    print("foo is running")


def log(func):
    print("{} is running".format(func))
    func()

def log2(func):
    print("{} is running".format(func)) #2. zhixing
    return func  # 3. 返回一个函数对象

@log2  # 1. 执行装饰器函数
def foo2():  # 4. 调用函数
    print("this is a func, foo2")

foo2()