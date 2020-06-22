'''
写一个Bicycle（自行车）类，有run（骑行）方法，调用时显示骑行历程km（骑行里程为传入的数字）：
再写一个电动车类EBicycle继承自Bicycle,添加电池电量 valume 属性通过，参数传入，同时有两个方法：
1. fill_charge(vol)用来充电，vol为电量
2. run(km)方法用于骑行，每骑行10km消耗电量1度，
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数,显示骑行结果
'''

# 定义了一个Bicycle类
class Bicycle:
    # 定义了一个run方法，需要传入一个km参数
    def run(self, km):
        print("自行车骑的里程数为{}".format(km))

# 初始化 定义一个新的类，继承Bicycle类 括号中为父类
class EBicycle(Bicycle):
    # 类的传参，用init函数，放类的初始化一些参数
    def __init__(self, volume):
        # 实例变量 用self.变量名
        self.valume = volume

    def get_valume(self):
        print("当前电量为", self.valume)

    def fill_charge(self, vol):
        print("充电的电量为", vol)

    def run(self, km):
        # 电量支持的最大里程
        e_mails = self.valume*10
        # 假如电瓶有10度电，我们支持的最大里程数就是10*10=100
        mails = km - e_mails
        if mails <= 0:
            print("电瓶车骑了", km)
        else:
            # 因为子类中有一个run，把父类中的run覆盖掉了
            # self.run()
            # 应该传入的参数是除了骑电瓶车的里程数
            print("电瓶车骑了", e_mails)
            # 调用父类中的run方法 super.
            super().run(mails)

    # pass 占位符 起不到任何作用
    pass

# 在类初始化的时候，给init中定义的参数传参 一般只有一个init
mybike = EBicycle(10)
mybike.run(200)