# Design a HashMap without using any built-in hash table libraries.
# Time Complexity = O(1), Space Complexity = O(n)
# Leetcode = 706

class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Insert new key
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        index = self._hash(key)

        for k, v in self.buckets[index]:
            if k == key:
                return v

        return default

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return v

        raise KeyError(key)

    def contains(self, key):
        index = self._hash(key)

        return any(k == key for k, _ in self.buckets[index])

    def __len__(self):
        return self.size
        
        
        
m = HashMap()

m.put("name", "Alice")
m.put("age", 25)

print(m.get("name"))      
print(m.get("city"))       
print(m.contains("age"))   

m.put("age", 26)
print(m.get("age"))        

m.remove("name")
print(m.contains("name"))  
