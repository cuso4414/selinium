'''
装饰器何时执行？
'''
# 定义了一个列表
regitry = []

#  定义了一个函数，函数需要传入一个 参数（函数对象）

def register(func):
    print("register is", func)
    # 把函数对象存入 regitry列表中
    regitry.append(func)
    # 返回一个函数对象
    return func

@register
def f1():
    print("f1")

@register
def f2():
    print("f2")

def f3():
    print("f3")

if __name__ == '__main__':
    print("running main()")
    print("regitry->", regitry)
    f1()
    f2()
    f3()


