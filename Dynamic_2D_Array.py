# Dynamic 2D Array

rows = int(input("How many rows do you want? "))
cols = int(input("How many columns do you want? "))

stack = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        stack[i][j] = int(input(f"Enter element at row {i}, column {j}: "))

print("\n2D Array:")
print(stack)
