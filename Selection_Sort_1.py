# Sort an array using Selection sort 
# Time Complexity = O(n²), Space Complexity = O(1)

li = list(map(int, input("Enter the List:").split()))

for i in range(len(li)):
    small = i
    
    for j in range(i+1, len(li)):
        if li[small] > li[j]:
            small = j
            
    li[i], li[small] = li[small], li[i]

print(li)
