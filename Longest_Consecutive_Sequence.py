# Given an unsorted integer array, find the length of the longest sequence of consecutive integers in O(n) time without sorting the array.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 128

nums = list(map(int,input("Enter the List :").split()))

count = 0

hset = set(nums)

for i in hset:
    
    if i - 1 not in hset:
        
        temp = 0
        
        while i in hset:
            temp += 1
            i += 1
            
        if count < temp:
            count = temp
        
print(count)
