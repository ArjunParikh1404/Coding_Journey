# Merge sort
# Time Complexity = O(n log n), Space Complexity = O(n)

nums = list(map(int, input("Enter the array:").split()))

def split(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    
    left = split (arr[:mid])
    right = split (arr[mid:])
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
nums = split(nums)

print(nums)
