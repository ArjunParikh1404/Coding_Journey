# Move all elements not equal to val to the front of the array and return their count.
# Example : nums = [0,1,2,2,3,0,4,2] , val = 2
# Time Complexity : O(n), Space Complexity : o(1) - Leetcode 27

nums = list(map(int,input("Enter the Array : ").split()))

val = int(input("Enter the value to remove: "))

p1 = 0
p2 = len(nums) - 1

while p1 <= p2:
    if nums[p1] == val:
        nums[p1],nums[p2] = nums[p2],nums[p1]
        p2 -= 1
    else:
        p1 += 1
        
k = p2 + 1 

print(nums)
print(k)
