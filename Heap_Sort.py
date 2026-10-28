# Heap sort 
# Time Complexity = O(n log n), Space Complexity = O(log n)

def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and nums[largest] < nums[left]:
        largest = left
        
    if right < n and nums[largest] < nums[right]:
        largest = right
        
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
    
        heapify(nums, n, largest)
    
    
def heap_sort(nums):
    n = len(nums)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        
        heapify(nums, i, 0)
        
    return nums

nums = list(map(int, input("Enter the list:").split()))

nums = heap_sort(nums)

print(nums)
