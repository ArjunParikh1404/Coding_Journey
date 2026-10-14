# Given a list of integers, find and print the largest element in the list.
# Time Complexity = O(n), Space Complexity = O(1)

nums = list(map(int, input("Enter the list:").split()))

high = 0

for i in nums:
    if i > high:
        high = i
        
print(high)
