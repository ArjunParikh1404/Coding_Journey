# Given an array of up to 10⁶ non-negative integers, sort the array in ascending order using Radix Sort without using any built-in sorting functions.
# Time Complexity = O(d × (n + 10)), Space Complexity = O(n + 10)

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

    return(op)


def radix(arr):

    if len(arr) == 0:
        return arr

    for i in range(len(str(max(arr)))):
        arr = counting(arr, i)

    return(arr)


nums = list(map(int, input("Enter the list :").split()))

nums = radix(nums)

print(nums)
