# Replace every element with the greatest element to its right, and replace the last element with -1.
# Time Complexity = O(n²) , Space Complexity = O(1)
# Leetcode = 1299

arr = list(map(int, input("Enter the Array :").split()))
temp = 0

for i in range(len(arr)):
    if i == len(arr) - 1:
        arr[i] = -1
    else: 
        for j in range(i+1, len(arr)):
            if arr[j] > temp:
                temp = arr[j]
        arr[i] = temp
        temp = 0

print(arr)
