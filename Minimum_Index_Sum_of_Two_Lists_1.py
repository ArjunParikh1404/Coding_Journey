# Find all common strings between two lists whose sum of indices is the minimum.
# Time Complexity = O(n + m), Space Complexity = O(n + m)
# Leetcode = 599

list1 = list(map(str, input("Enter the first list :").split()))

list2 = list(map(str, input("Enter the second list :").split()))

map1 = {}
map2 ={}
total = float("inf")
op = []

for key, val in enumerate(list1):
    map1[val] = key
    
for key, val in enumerate(list2):
    map2[val] = key
    
for i in list1:
    if i in map2:
        if total > map1[i] + map2[i]:
            op.clear()
            op.append(i)
            total = map1[i] + map2[i]
            
        elif total == map1[i] + map2[i]:
            op.append(i)

print(op)
