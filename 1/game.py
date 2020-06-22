'''
一个回合制游戏，每个角色都有hp 和 power,hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为2002
定义一个fight方法：
final_hp = hp-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
'''

class Game():
    def __init__(self):
        self.hp = 1000
        self.power = 200

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp > enemy_final_hp:
            print("敌人赢了")
        else:
            raise Exception("No peace,keep fighting")

mygame = Game()
mygame.fight(1000, 199)



'''
代码优化——继承
使用传参的方式传入hp和血量
第二个角色，他叫后裔，后裔继承了角色的hp 和 power。并多了护甲属性
重新定义另一个defense方法：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
'''



'''
多回合制游戏进行
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
