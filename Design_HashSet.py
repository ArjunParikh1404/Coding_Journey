# Design a HashSet from scratch that supports add, contains, and remove operations without using built-in hash table libraries.
# Time Complexity = O(1), Space Complexity = O(n)
# Leetcode = 705

class HashSet:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Don't add if key already exists
        for k in bucket:
            if k == key:
                return

        # Add new key
        bucket.append(key)
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, k in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return

        raise KeyError(key)

    def contains(self, key):
        index = self._hash(key)

        for k in self.buckets[index]:
            if k == key:
                return True

        return False

    def __len__(self):
        return self.size


# Testing

s = HashSet()

s.add("Alice")
s.add("Bob")
s.add("Charlie")

print(s.contains("Alice"))      
print(s.contains("David"))      

s.add("Alice")                  
print(len(s))               

s.remove("Bob")
print(s.contains("Bob"))

print(len(s))
