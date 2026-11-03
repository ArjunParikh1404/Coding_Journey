# Counting sort
# Time Complexity = O(n + k), Space Complexity = O(n + k)

nums = list(map(int, input("Enter the list: ").split()))

max_num = max(nums)
min_num = min(nums)

k = max_num - min_num + 1
count = [0] * k

for num in nums:
    count[num - min_num] += 1

sorted_nums = []

for i in range(k):
    for j in range(count[i]):
        sorted_nums.append(i + min_num)

print("Sorted list:", sorted_nums)
