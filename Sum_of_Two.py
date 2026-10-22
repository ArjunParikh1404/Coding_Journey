# Given a list of integers and a target value, find and return the indices of two distinct elements whose sum equals the target, using a hash map for efficient lookup.
# Time Complexity = O(n), Space Complexity = O(n)

nums = list(map(int, input("Enter the list :").split()))

target = int(input("Enter the target:"))

hmap = {}

op = []

for i,ch in enumerate(nums):
    find = target - ch
    
    if find in hmap:
        op.append(hmap[find])
        op.append(i)
        break
    
    else:
        hmap[ch] = i
        
print(op)
