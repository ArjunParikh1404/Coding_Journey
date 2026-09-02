# Find the index of the first non-repeating character in a string, or return -1 if none exists.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 387

s = str(input("Enter the string :"))

hmap = {}

for i in s:
    if i in hmap:
        hmap[i] += 1
    else:
        hmap[i] = 1
        
for ind, val in enumerate(s):
    if hmap[val] == 1:
        print(ind)
        break
else:
    print("-1")
