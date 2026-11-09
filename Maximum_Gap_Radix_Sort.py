# Given an unsorted array of non-negative integers, find the maximum difference between any two consecutive elements after sorting the array. 
# Time Complexity = O(d × n), Space Complexity = O(n)

def counting(arr, exp):

    res = [0] * 10

    for i in arr:
        count = (i // 10 ** exp) % 10

        res[count] += 1

    for j in range(1, len(res)):
        res[j] += res[j - 1]

    op = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // 10 ** exp) % 10

        op[res[digit] - 1] = arr[i]
        res[digit] -= 1

    return op

def radix(arr):

    for i in range(len(str(max(arr)))):
        arr = counting(arr, i)

    return arr

def maximumGap(nums):

    if len(nums) < 2:
        return 0

    nums = radix(nums)

    gap = 0

    for i in range(1, len(nums)):

        diff = nums[i] - nums[i - 1]

        if diff > gap:
            gap = diff

    return gap


nums = list(map(int, input("Enter the list : ").split()))

print("Maximum Gap :", maximumGap(nums))
