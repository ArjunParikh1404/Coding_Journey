# Given a list of strings, group all anagrams together and return the result as a list of lists.
# Time Complexity = O(n×klogk), Space Complexity = O(n×k)
# Leetcode = 49

strs = list(map(str, input("Enter the List :").split()))

hmap = {}

for ch in strs:
    
    key = ''.join(sorted(ch))
    
    if key not in hmap:
        hmap[key] = []
        
    hmap[key].append(ch)
    
print(list(hmap.values()))
