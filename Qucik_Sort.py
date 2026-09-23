# Sort the array using Qucik Sort.
# Time Complexity = O(n²), Space Complexity = O(n²)
# Leetcode = 912

nums = list(map(int, input("Enter the list :").split()))

def qucik_sort(arr):
    if len(arr) <= 1:
        return arr
        
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    left = qucik_sort(left)
    right = qucik_sort(right)
    
    return left + [arr[0]] + right
    
nums = qucik_sort(nums)

print(nums)
