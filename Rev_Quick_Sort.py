# Sort a list of integers in ascending order using the Quick Sort algorithm.
# Time Complexity = O(n²), Space Complexity = O(n²)
 
nums = list(map(int,input("Enter the List :").split()))

def quick(arr):
    
    if len(arr) <= 1:
        return arr
        
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
            
    left = quick(left)
    right = quick(right)
    
    result = left + [pivot] + right

    return result


nums = quick(nums)

print(nums)
