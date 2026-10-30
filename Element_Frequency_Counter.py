# Write a Python program to count the frequency of each element in a given list.
# Time Complexity = O(n), Space Complexity = O(n)

nums = list(map(int, input("Enter the List:").split()))

hset = {}

for i in nums:
    if i in hset:
        hset[i] += 1
    else:
        hset[i] = 1
    
print(hset)
