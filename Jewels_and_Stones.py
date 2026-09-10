# Given two strings jewels and stones, count how many characters in stones are also present in jewels, with case sensitivity.
# Time Complexity = O(n + m), Space Complexity = O(n)
# Leetcode = 771

jewels = str(input("Enter the list of jewels :"))

stones = str(input("Enter the list of stones :"))

hset = set(jewels)
total = 0
    
for s in stones:
    if s in hset:
        total += 1
        
print(total)
