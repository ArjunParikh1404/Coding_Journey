# Given an integer array nums and an integer k, return the k most frequent elements in the array.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 347

nums = list(map(int, input("Enter the list : ").split()))

k = int(input("Enter the value of k : "))

hmap = {}

for i in nums:
    if i in hmap:
        hmap[i] += 1
    else:
        hmap[i] = 1

# bucket sort
buckets = [[] for _ in range(len(nums) + 1)]

for num, freq in hmap.items():
    buckets[freq].append(num)

result = []

for i in range(len(buckets) - 1, 0, -1):
    for num in buckets[i]:
        result.append(num)

        if len(result) == k:
            break

    if len(result) == k:
        break

print("Top", k, "frequent elements:", result)
