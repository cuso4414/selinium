# 对game改造
# 改造，虽然减少了代码量，但是尽量不要这样改造。子类和父类之间要尽量解耦，子类的逻辑，不要写在父类
class Game:
    def __init__(self, hp=1000, power=2000, enemy_power=2000, enemy_hp=1000, denfense=100):
        self.hp = 1000
        self.power = 200
        self.final_hp = self.hp - enemy_power
        self.enemy_final_hp = enemy_hp - self.power
        self.houyi_hp = self.hp + denfense - enemy_power

    def fight(self):
        if self.houyi_hp > self.enemy_final_hp:
            print("我赢了")
        elif self.houyi_hp < self.enemy_final_hp:
            print("后裔赢了")
        else:
            print("平局")

class HouYi(Game):

    pass


houyi = HouYi()
houyi.fight()