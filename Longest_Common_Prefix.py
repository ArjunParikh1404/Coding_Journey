# Given an array of strings, return the longest prefix common to all the strings; if none exists, return an empty string ("").
# Time Complexity = O(n × m), Space Complexity = O(1)
# Leetcode = 14

strs = list(map(str, input("Enter strings separated by spaces: ").split()))

result = str(strs[0])

for i in strs:
    j = 0
    while j <= len(i)-1 and j <= len(result)-1:
        if i[j] != result[j]:
            result = result[:j]
            break
        j += 1
    
    result = result[:j]
    
print(result)
