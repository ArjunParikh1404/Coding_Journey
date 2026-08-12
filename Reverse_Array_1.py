# Reverse the given array and print the reversed array.
# Time Complexity = O(n), Space Complexity = O(n)

nums = list(map(int, input("Enter the Array : ").split()))

nums = nums[::-1]

print(nums)
