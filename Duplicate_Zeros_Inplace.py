# Given a fixed-size array, duplicate each zero in-place and shift remaining elements right without exceeding array length.
# Leetcode = 1089

arr = list(map(int, input("Enter the Array : ").split()))

zeros = arr.count(0)
real = len(arr) - 1
virtual = len(arr) - 1 + zeros

while real < virtual:
    if virtual < len(arr):
        arr[virtual] = arr[real]
        
    if arr[real] == 0:
        virtual -= 1
        if virtual < len(arr):
            arr[virtual] = 0
    
    real -= 1
    virtual -= 1
    
print(arr)
