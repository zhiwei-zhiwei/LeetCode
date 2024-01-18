import ast
import random

class RandomizedSet:
    def __init__(self):
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            del self.hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.hashmap.keys()))


operations = input()
operations = operations.strip('[]').replace('"', '').split(',')
actions = input()
actions = ast.literal_eval(actions)
print(actions[1][0])

startPoint = False
if operations[0] == "RandomizedSet":

    startPoint = True

res = []

if startPoint == True:
    obj = RandomizedSet()
    res.append(None)
    for i in range(1, len(operations)):
        if operations[i] == "insert":
            res.append(obj.insert(actions[i][0]))
        elif operations[i] == "remove":
            res.append(obj.remove(actions[i][0]))
        else:
            res.append(obj.getRandom())

print(res)

