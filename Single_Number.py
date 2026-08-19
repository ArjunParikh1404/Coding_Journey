# Find the single element in an array where every other element appears exactly twice.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 136

nums = list(map(int, input("Enter the array ").split()))

s = set()

for i in nums:
    if i not in s:
        s.add(i)
    else:
        s.remove(i)
        
print(s.pop())
