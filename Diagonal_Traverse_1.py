# Given a matrix, return all its elements by traversing the diagonals alternately from bottom-to-top and top-to-bottom order.
# Time Complexity = O(m × n), Space Complexity = O(m × n)
# Leetcode = 498

m, n = map(int, input("Enter rows and columns: ").split())

mat = []

print("Enter matrix elements:")
for i in range(m):
    mat.append(list(map(int, input().split())))
    
result = []

row, col = 0, 0
up = True

while len(result) < m*n:
    result.append(mat[row][col])
    
    if up:
        if col == n - 1:
            row += 1
            up = False
        elif row == 0:
            col += 1
            up = False
        else:
            col += 1
            row -= 1
            
    else:
        if row == m - 1:
            col += 1
            up = True
        elif col == 0:
            row += 1
            up = True
        else:
            row += 1
            col -= 1
            
print(result)
