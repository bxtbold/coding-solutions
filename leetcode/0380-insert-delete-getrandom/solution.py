import random

class RandomizedSet:
    """
    RUNTIME: 571 ms (81.63%)
    MEMORY: 61.4 MB (32.70%)
    """
    def __init__(self):
        self.hashset = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashset:
            self.hashset[val] = 0
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashset:
            del self.hashset[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.hashset.keys()))