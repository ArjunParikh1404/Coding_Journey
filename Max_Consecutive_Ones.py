# Finds and prints the maximum number of consecutive 1s in a user-provided array.

num = list(map(int, input("Enter the elements of the array").split()))
total = 0
temp = 0

for i in num:
    if i == 1:
        total += 1
    else:
        total = 0
    
    if total > temp:
            temp = total    
    
print(temp)
