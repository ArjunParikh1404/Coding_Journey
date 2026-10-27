# Heap sort = max heap + swap
# The root of a Max Heap contains the largest element, so we swap it with the last element in the unsorted portion of the array. After each swap, we reduce the size of the unsorted portion and repeat the process. We don't need to sort the entire heap; we only need to ensure that the maximum element reaches the root before each swap.
# Time Complexity = O(n²), Space Complexity = O(1)

nums = list(map(int, input("Enter the list:").split()))

for x in range(len(nums)-1, 0, -1):
    
    for i in range(x, 0, -1):
        if nums[i] > nums[(i-1) // 2]:
            nums[i], nums[(i-1) // 2] = nums[(i-1) // 2], nums[i]
            
    nums[0], nums[x] = nums[x], nums[0]
    
print(nums)
