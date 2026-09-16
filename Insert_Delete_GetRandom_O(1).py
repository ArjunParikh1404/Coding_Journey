# Implement a RandomizedSet that supports insert, remove, and getRandom operations in average O(1) time, with getRandom() returning each element with equal probability.
# Time Complexity = O(1), Space Complexity = O(1)
# Leetcode = 380

import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.pos[last] = idx

        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


obj = RandomizedSet()

n = int(input("Enter number of operations: "))

for _ in range(n):
    operation = input("Enter operation (insert/remove/getRandom): ").strip()

    if operation == "insert":
        val = int(input("Enter value: "))
        print(obj.insert(val))

    elif operation == "remove":
        val = int(input("Enter value: "))
        print(obj.remove(val))

    elif operation == "getRandom":
        print(obj.getRandom())

    else:
        print("Invalid operation")
