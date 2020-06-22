import json

class PracticeJson:
    def __init__(self):
        self.data = {"a":1, "b":2}

    def practice_dumps(self):
        # print("dumps之前")
        # print(type(self.data))
        # print("dumps之后")
        # print(type(json.dumps(self.data)))
        print(json.dumps(self.data, sort_keys=True, indent=4))

    def practice_dump(self):
        with open("./demo.json", "w") as fs:
            json.dump(self.data, fp=fs)

    def practice_load(self):
        json_data = json.dumps(self.data)
        print("loads之前")
        print(type(json_data))
        print("loads之后")
        print(type(json.loads(json_data)))

    def practice_loads(self):
        print(json.load(open("demo.json")))

pj = PracticeJson()
pj.practice_dumps()