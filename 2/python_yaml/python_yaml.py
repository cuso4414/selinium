import yaml
data = [1, 2, 3]

# data = {"a":1, "b":2, "c": {"a":4, "b":5, "z":6}}

print(yaml.safe_load(open("./demo.yaml")))
