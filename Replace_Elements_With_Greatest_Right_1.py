# Replace every element with the greatest element to its right, and replace the last element with -1.
# Time Complexity = O(n) , Space Complexity = O(1)
# Leetcode = 1299

arr = list(map(int, input("Enter the Array : ").split()))

high = arr[len(arr) - 1]
X = high

for i in range(len(arr)-2,-1,-1):
    X = high
    if arr[i] > high:
        high = arr[i]
        
    arr[i] = X
    
arr[len(arr) - 1] = -1
print(arr)
