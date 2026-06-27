# Checks if the array contains any pair of numbers where one number is exactly double the other, and prints True if found; otherwise, False.
# Time Complexity: O(n²), Space Complexity: O(1)
# Leetcode = 1346

arr = list(map(int, input("Enter the Array :").split()))
found = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] / 2 == arr[j] or arr[i] * 2 == arr[j]:
            found = True
            break
    if found:
        break
        
print(found)
