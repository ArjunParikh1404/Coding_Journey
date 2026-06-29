# Traverse the array once to verify it strictly increases to one peak and then strictly decreases until the end.
# Time complexity = O(n), Space complexity = O(1)
# Leetcode - 941

arr = list(map(int, input("Enter the Array :").split()))

p1 = 0

if len(arr) < 3:
    print("False") 
else : 
    while p1 < len(arr) - 1 and arr[p1] < arr[p1 + 1]:
        p1 += 1
        
    if p1 == 0 or p1 == len(arr) - 1:
        print("False")
    else:
        while p1 < len(arr) - 1 and arr[p1] > arr[p1 + 1]:
            p1 += 1
        
        print("True" if p1 == len(arr) - 1 else "False")
