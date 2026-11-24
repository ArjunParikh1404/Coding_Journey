# Given a binary array nums, find the maximum length of a contiguous subarray with an equal number of 0s and 1s.
# Time Complexity = O(n), Space Complexity = O(n)

nums = list(map(int,input("Enter the List :").split()))

hmap = {0: -1}

count = 0
max_count = 0

for i in range(len(nums)):

    if nums[i] == 0:
        count -= 1
    else:
        count += 1

    if count in hmap:
        temp = i - hmap[count]

        if max_count < temp:
            max_count = temp

    else:
        hmap[count] = i

print(max_count)
