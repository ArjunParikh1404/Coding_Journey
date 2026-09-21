# Given a list of strings, group together strings that can be transformed into each other by shifting every character by the same number of positions.
# Time Complexity = O(N × L²), Space Complexity = O(N × L)
# Leetcode = 249

strs = list(map(str, input("Enter the list of string :").split()))

hmap = {}

for i in strs:
    key = ()
    for j in range(1,len(i)):
        val = (ord(i[j-1]) - ord(i[j])) % 26
        key = key + (val,)
        
    if key not in hmap:
        hmap[key] = []
        
    hmap[key].append(i)
    
print(hmap)   
