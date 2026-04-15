# Computes the maximum amount that can be robbed without taking adjacent houses.
# Uses an optimized dynamic programming approach with constant space.

def rob(nums):
    prev, curr = 0, 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr

print(rob([2,7,9,3,1]))
