# 生成器
def provider():
    for i in range(5):
        print("before")
        yield i   # return i   暂时操作  并且记住上一次的执行位置
        print("after")

p = provider()
print(next(p))
print(next(p))
