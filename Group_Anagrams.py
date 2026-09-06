# Group strings that are anagrams of each other into separate groups.
# Time Complexity = O(n × k log k), Space Complexity = O(n × k)
# Leetcode = 49

strs = list(map(str,input("Enter the list :").split()))

hmap = {}

for i in strs:
    key = ''.join(sorted(i))
    
    if key not in hmap:
        hmap[key] = []
    
    hmap[key].append(i)
    
print(list(hmap.values()))
