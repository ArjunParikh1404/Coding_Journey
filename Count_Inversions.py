# Count Inversions using Merge Sort
# Time Complexity = O(n log n), Space Complexity = O(n)

nums = list(map(int, input("Enter the list : ").split()))

def split(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left, left_count = split(left)
    right, right_count = split(right)

    merged, merge_count = merge(left, right)

    total_count = left_count + right_count + merge_count

    return merged, total_count


def merge(left, right):
    sorted_arr = []
    i = j = 0
    count = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1

        else:
            sorted_arr.append(right[j])

            count += len(left) - i

            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr, count


nums, inversions = split(nums)

print("Sorted array :", nums)
print("Inversions   :", inversions)
