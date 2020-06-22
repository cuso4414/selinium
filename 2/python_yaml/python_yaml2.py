'''
讲上节课excel中的列表信息使用yaml进行存放并读取
'''
import yaml

class PythonYaml:
    def __init__(self):
        self.data = yaml.safe_load(open("./data.yaml"))
        # print(self.data)

    def read_list(self):
        # height = [180, 160, 170, 155]
        # weight = [60, 55, 60, 80]
        # 循环 key值为“height”的value,并求出来value的长度，作为循环的次数
        for i in range(len(self.data["height"])):
            print("身高是{}，体重是{}".format(self.data["height"][i], self.data["weight"][i]))

if __name__ == "__main__":
    py1 = PythonYaml()
    py1.read_list()

