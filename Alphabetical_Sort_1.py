# Given a list of strings, sort them in alphabetical order using the Selection Sort algorithm without using Python’s built-in sorting functions.
# Time Complexity = O(n²), Space Complexity = O(1)

li = list(map(str, input("Enter the list :").split()))

for i in range(len(li)):
    small = i
    
    for j in range(i + 1, len(li)):
        if li[j] < li[small]:
            small = j

    li[i], li[small] = li[small], li[i]
    
print(li)
