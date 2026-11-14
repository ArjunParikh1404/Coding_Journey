# Implement Lomuto Partition to place smaller elements left and larger elements right of the last-element pivot.
# Time Complexity = O(n), Space Complexity = O(1)

nums = list(map(int, input("Enter the list : ").split()))

def lomuto_partition(arr):
    pivot = arr[-1]

    i = -1

    for j in range(len(arr) - 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]

    return i + 1


pivot_index = lomuto_partition(nums)

print("Sorted partition :", nums)
print("Pivot index :", pivot_index)
