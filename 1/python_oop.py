class Turtle:
    # 类变量，静态变量
    legs = 4
    mouths = 1
    eye = 2

    # 类中的函数称为方法，动态方法
    def bite(self):
        print("乌龟咬人")

    def clumb(self):
        print("爬走")
# 直接调用类属性
print(Turtle.eye)
print(Turtle.bite)

# 类实例化
mytutle = Turtle()

# 直接调用实例对象中的属性
print(mytutle.eye)
mytutle.bite()



class QiaoFeng():
    height = 180
    face = "handsome"

    def fight_xlsbz(self):
        print("降龙十八掌")
