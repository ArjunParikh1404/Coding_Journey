# Given a matrix, return all its elements by traversing the diagonals alternately from bottom-to-top and top-to-bottom order.
# Time Complexity = O((m+n)mn), Space Complexity = O(mn)
# Leetcode = 498

row = int(input("Enter the number of row :"))

col = int(input("Enter the number of col :"))

matrix = []

for i in range(row):
    temp = []
    for j in range(col):
        temp.append(int(input(f'Enter the value of {i}th row and {j}th col :')))
    matrix.append(temp)

last = row + col - 1
ans = []

for i in range(last):
    temps = []
    for j in range(row):
        for k in range(col):
            if i == j + k:
                temps.append(matrix[j][k])
    
    if i % 2 == 0:
        ans.extend(temps[::-1])
    else:
        ans.extend(temps)
        
print(ans)
