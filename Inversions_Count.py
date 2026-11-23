# Count inversions in an array using Merge Sort.
# Given an array of integers, count the number of pairs (i, j) such that i < j and arr[i] > arr[j].
# Time Complexity = O(n log n), Space Complexity = O(n)

nums = list(map(int, input("Enter the list : ").split()))

def split(arr):
  if len(arr) <= 1:
    return arr, 0

  mid = len(arr) // 2  

  left = arr[:mid]
  right = arr[mid:]

  left, count_left = split(left)
  right, count_right = split(right)

  sorted_arr, count_merge = merge(left, right)

  return sorted_arr, count_left + count_right + count_merge

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

print("Sorted Array :", nums)
print("Inversion Count :", inversions)  
