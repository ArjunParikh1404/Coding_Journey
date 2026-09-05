# Design a logger that prints a message only if the same message has not been printed in the previous 10 seconds.
# Time Complexity = O(1), Space Complexity = O(n)
# Leetcode = 359

class Logger:
    def __init__(self):
        self.hmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hmap:
            self.hmap[message] = timestamp
            return True

        if timestamp - self.hmap[message] >= 10:
            self.hmap[message] = timestamp
            return True

        return False

# Tests
logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))   # True
print(logger.shouldPrintMessage(2, "bar"))   # True
print(logger.shouldPrintMessage(3, "foo"))   # False
print(logger.shouldPrintMessage(8, "bar"))   # False
print(logger.shouldPrintMessage(10, "foo"))  # False
print(logger.shouldPrintMessage(11, "foo"))  # True
