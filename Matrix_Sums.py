import numpy as np

# Input for rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create empty matrix
matrix = []

print("\nEnter matrix elements row by row:")

# Input matrix elements
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)

# Convert to NumPy array
matrix = np.array(matrix)

print("\nMatrix:")
print(matrix)

# Row sums
row_sums = np.sum(matrix, axis=1)

print("\nRow Sums:")
for i, value in enumerate(row_sums):
    print(f"Row {i+1} Sum = {value}")

# Column sums
col_sums = np.sum(matrix, axis=0)

print("\nColumn Sums:")
for i, value in enumerate(col_sums):
    print(f"Column {i+1} Sum = {value}")
