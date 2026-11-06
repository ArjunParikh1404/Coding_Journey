# Given an array of integers, find the element that occurs the least number of times using Counting Sort.
# Time Complexity = O(n + k), Space Complexity = O(k)

def counting(arr):

    minimum = min(arr)
    maximum = max(arr)

    res = [0] * (maximum - minimum + 1)

    for i in arr:
        res[i - minimum] += 1

    return res, minimum


def least(arr):

    res, minimum = counting(arr)

    least_freq = len(arr) + 1
    element = None

    for i in range(len(res)):

        if res[i] > 0 and res[i] < least_freq:

            least_freq = res[i]
            element = i + minimum

    return element

arr = list(map(int, input("Enter array elements: ").split()))

result = least(arr)

print("Least frequent element:", result)
