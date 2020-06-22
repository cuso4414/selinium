class Drawing:
    area = 12
    style = "North Europe"
    # 私有属性 私有变量
    __style2 = "china style"

    def sleep(self):
        # 在类中的其他方法中可以调用类私有属性
        print(self.__style2)
        print("房子可以用来睡觉")

    def cook(self):
        print("房子可以用来做饭")

    # 私有属性，私有方法
    def __sleepat_bathroom(self):
        print("我在厕所")
        # 在方法里调用其他方法 用self.就可以调用其他属性和方法
        self.sleep()

a = 1
my_house = Drawing()
my_house.sleep()

# 通过name重写的方法就可以调用私有属性（加上下划线和类名后再调用），但是不建议这样使用
my_house._Drawing__sleepat_bathroom()
my_house._Drawing__style2

Bob_house = Drawing()
Bob_house.sleep()

# class相当于图纸  实例化对象相当于根据图纸造出来的房子，每个房子很像但是不一样 self相当于门牌号
