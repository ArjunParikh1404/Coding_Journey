# Given a list of dates in DD-MM-YYYY format, sort them in chronological order (earliest to latest) using Radix Sort.
# Time Complexity = O(d × n), Space Complexity = O(n)

def counting(arr, exp, div, base):

    res = [0] * base

    for i in arr:
        count = (i[exp] // div) % base

        res[count] += 1

    for j in range(1, len(res)):
        res[j] += res[j - 1]

    op = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i][exp] // div) % base

        op[res[digit] - 1] = arr[i]
        res[digit] -= 1

    return op

def radix(arr):

    for i in range(2):
        arr = counting(arr, 0, 10 ** i, 10)

    for i in range(2):
        arr = counting(arr, 1, 10 ** i, 10)

    for i in range(4):
        arr = counting(arr, 2, 10 ** i, 10)

    return arr

dates = input("Enter dates (DD-MM-YYYY): ").split()

# Convert dates into [DD, MM, YYYY]
dates = [list(map(int, date.split("-"))) for date in dates]

dates = radix(dates)

for i in dates:
    print(f"{i[0]:02d}-{i[1]:02d}-{i[2]:04d}")
