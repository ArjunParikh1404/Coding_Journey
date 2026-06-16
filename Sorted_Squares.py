# Read integers, square them, and output the sorted squared values
# Time Complexity = O(n log n), Space Complexity = O(n)

nums = list(map(int,input("Enter the array :").split()))

nums = sorted(x*x for x in nums)

print(nums)
