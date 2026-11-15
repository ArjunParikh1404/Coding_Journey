# Given a sorted array and a new element, insert the element into its correct position while maintaining the sorted order.
# Time Complexity = O(n), Space Complexity = O(1)

nums = list(map(int, input("Enter the list :").split()))
ele = int(input("Enter the element to insert :"))

nums.append(ele)

a = len(nums) - 1

while nums[a - 1] > nums[a] and a > 0:
    nums[a - 1], nums[a] = nums[a], nums[a - 1]

    a -= 1

print(nums)
