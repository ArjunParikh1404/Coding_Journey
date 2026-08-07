# Given an integer array nums and a non-negative integer k, rotate the array to the right by k positions, modifying the array in-place if possible.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 189
# Reversing trick

nums = list(map(int, input("Enter the array :").split()))

k = int(input("Enter the value of k :"))

k %= len(nums)

def rev(first,last):
    while first < last:
        nums[first], nums[last] = nums[last], nums[first]
        first += 1
        last -= 1
    return nums

rev(0, len(nums) - 1)

rev(0, k - 1)

rev(k, len(nums) - 1)
    
print(nums)
