# Find all common strings between two lists whose sum of indices is the minimum.
# Time Complexity = O(n + m), Space Complexity = O(n)
# Leetcode = 599

list1 = list(map(str, input("Enter the first list :").split()))

list2 = list(map(str, input("Enter the second list :").split()))

map1 = {}
total = float("inf")
op = []

for key,val in enumerate(list1):
    map1[val] = key
    
for key,val in enumerate(list2):
    if val in map1:
        if total > key + map1[val]:
            op.clear()
            op.append(val)
            total = key + map1[val]
            
        elif total == key + map1[val]:
            op.append(val)
            
print(op)
