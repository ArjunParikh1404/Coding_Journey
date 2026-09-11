# Find the length of the longest substring containing no duplicate characters.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 3

s = str(input("Enter the string :"))

hset = set()

big = 0
left = 0

for right in range(len(s)):
    while s[right] in hset:
        hset.remove(s[left])
        left += 1
    
    hset.add(s[right])
    
    big = max(big, right - left + 1)
    
print(big)
