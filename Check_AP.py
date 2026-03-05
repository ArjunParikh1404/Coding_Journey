# Program to check whether the given list of numbers forms an Arithmetic Progression (AP).

def isAP(arr):
    n = len(arr)
    if n <= 1:
        return True
    
    arr.sort()
    d = arr[1] - arr[0]
    
    for i in range(2, n):
        if arr[i] - arr[i-1] != d:
            return False
    return True

# Taking input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

if isAP(arr):
    print("The series is in AP")
else:
    print("The series is NOT in AP")
