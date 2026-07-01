# Given an Array of integers, return an Array where every element at an even-indexed position is squared.
# Time Complexity = O(n), Space Complexity = O(1)

arr = list(map(int, input("Enter the Array : ").split()))

for i in range(0, len(arr), 2):
    arr[i] *= arr[i]
    
print(arr)
