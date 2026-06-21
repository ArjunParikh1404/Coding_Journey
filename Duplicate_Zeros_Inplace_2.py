# Given a fixed-size array, duplicate each zero in-place and shift remaining elements right without exceeding array length.
# Time Complexity = O(n^2)   Space Complexity = O(1)

arr = list(map(int, input("Enter the Array : ").split()))
i = 0

while i <= len(arr) - 1:
    if arr[i] == 0:
        arr.insert(i+1 , 0)
        arr.pop(len(arr)-1)
        i += 1
    i += 1
        
print(arr)
