# Counting sort
# Time Complexity = O(n + k), Space Complexity = O(n + k)

nums = list(map(int, input("Enter the list: ").split()))

count = [0] * (max(nums) + 1)

for i in nums:
    count[i] += 1
    
nums = []

for i in range(len(count)):
    for j in range(count[i]):
        nums.append(i)
        
print(nums)
