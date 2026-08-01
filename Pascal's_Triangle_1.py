# Given a non-negative integer rowIndex, return the rowIndexth (0-indexed) row of Pascal’s Triangle.
# Time Complexity = O(n²), Space Complexity = O(n²), Auxiliary Space = O(n)
# Leetcode = 119

rowIndex = int(input("Enter the row index : "))

row = [1]

for i in range(1, rowIndex + 1):
    new_row = [1]

    for j in range(1, i):
        new_row.append(row[j - 1] + row[j])

    new_row.append(1)
    row = new_row

print(row)
