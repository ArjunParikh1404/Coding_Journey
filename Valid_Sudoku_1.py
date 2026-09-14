# Determine whether a given 9×9 Sudoku board is valid by ensuring no digit repeats in any row, column, or 3×3 sub-box.
# Time Complexity = O(1), Space Complexity = O(1)
# Leetcode = 36

board = []

for i in range(9):
    row = input(f"Enter row {i + 1}: ").split()
    board.append(row)

hmap = {}

valid = True

for i in range(9):
    for j in range(9):
        value = board[i][j]

        if value == ".":
            continue

        # Check row
        row_key = f"row{i}"
        if row_key not in hmap:
            hmap[row_key] = set()

        if value in hmap[row_key]:
            valid = False
            break

        hmap[row_key].add(value)

        # Check column
        col_key = f"col{j}"
        if col_key not in hmap:
            hmap[col_key] = set()

        if value in hmap[col_key]:
            valid = False
            break

        hmap[col_key].add(value)

        # Check 3x3 box
        box_key = f"box{i // 3}{j // 3}"
        if box_key not in hmap:
            hmap[box_key] = set()

        if value in hmap[box_key]:
            valid = False
            break

        hmap[box_key].add(value)

    if not valid:
        break

print(valid)
