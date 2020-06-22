'''
代码优化——继承
使用传参的方式传入hp和血量
第二个角色，他叫后裔，后裔继承了角色的hp 和 power。并多了护甲属性
重新定义另一个defense方法：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
'''
from python_oo.game_game.game import Game

'''
多回合制游戏进行
'''

'''
调用模块-调用自己写的模块
'''
class HouYi(Game):
    def __init__(self):
        # 不加super()的话会导致子类中定义的init覆盖父类中的init
        super().__init__()
        self.denfense = 100

    def denfense1(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp + self.denfense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的血量是：", self.hp)
            print("敌人的血量是：", enemy_hp)
            if self.hp <= 0:
                print("我输了")
                break
            elif enemy_hp <= 0:
                print("敌人输了")
                break


houyi = HouYi()
houyi.denfense1(1000, 300)