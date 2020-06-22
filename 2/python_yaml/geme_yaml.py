'''
设定一个回合制2人对打游戏
每个人物都有hp,power,skill
hp代表血量，power代表攻击力，skill将攻击力翻倍
'''
import yaml

class Game:
    def __init__(self):
        infor = yaml.safe_load(open("./game.yaml"))
        print(infor)
        default = infor["default"]
        self.first = default[0]
        self.second = default[1]

        # 第二个人物
        self.first_hp = infor[self.first]["hp"]
        self.first_power = infor[self.first]["power"]
        self.first_skill = infor[self.first]["skill"]
        print(self.first_hp, self.first_power, self.first_skill)
        # 第二个人物
        self.second_hp = 1000
        self.second_power = 100
        self.second_skill = 2

    def fight(self):
        round = 0
        while True:
            print(self.first, self.first_power)
            print(self.second, self.second_hp)
            round += 1
            if round%3 == 0:
                self.first_hp = self.first_hp - self.second_power*self.second_skill
                self.second_hp = self.second_hp - self.first_power*self.first_skill
            else:
                self.first_hp = self.first_hp - self.second_power
                self.second_hp = self.second_hp - self.first_power
            if self.first_power <= 0:
                print("{} lose".format(self.first))
                break
            elif self.second_hp <= 0:
                print("{} lose".format(self.second))
                break

if __name__ == '__main__':
    mygame = Game()
    mygame.fight()

