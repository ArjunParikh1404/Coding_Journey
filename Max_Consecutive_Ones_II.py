# Given a binary array, return the maximum number of consecutive 1s you can obtain by flipping at most one 0 to 1.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode 487

nums = list(map(int, input("Enter the binary array : ").split()))

left = 0
zero = 0
answer = 0

for right in range(len(nums)):
    if nums[right] == 0:
        zero += 1
        
    while zero > 1:
        if nums[left] == 0:
            zero -= 1
        left += 1
        
    answer = max(answer, right - left + 1)
    
print(answer)
