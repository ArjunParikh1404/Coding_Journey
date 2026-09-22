# Sort an array using Merge Sort.
# Time Complexity = O(n log n), Space Complexity = O(n)
# Leetcode = 912

nums = list(map(int, input("Enter the list : ").split()))

def split(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2  
  
  left = arr[:mid]
  right = arr[mid:]

  left = split(left)
  right = split(right)

  return merge(left, right)


def merge(left, right):
  sorted_arr = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_arr.append(left[i])
      i += 1
    else:
      sorted_arr.append(right[j])
      j += 1

  sorted_arr.extend(left[i:])
  sorted_arr.extend(right[j:])

  return sorted_arr


nums = split(nums)
print(nums)
