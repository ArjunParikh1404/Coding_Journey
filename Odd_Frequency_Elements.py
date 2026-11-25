# Given a list of integers, find all elements that appear an odd number of times using a Python set.
# Time Complexity = O(n), Space Complexity = O(n)

nums = list(map(int, input("Enter the list :").split()))

hset = set()

for i in nums:
    if i in hset:
        hset.remove(i)
    else:
        hset.add(i)
        
print("Odd Frequency Elements:", hset)
