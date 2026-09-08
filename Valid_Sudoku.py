# Determine whether a given 9×9 Sudoku board is valid by ensuring no digit repeats in any row, column, or 3×3 sub-box.
# Time Complexity = O(1), Space Complexity = O(1)
# Leetcode = 36

board = []

for i in range(9):
    row = input(f"Enter row {i + 1}: ").split()
    board.append(row)


valid = True

# Check rows
for i in range(9):
    seen = set()

    for j in range(9):
        if board[i][j] == ".":
            continue

        if board[i][j] in seen:
            valid = False
            break

        seen.add(board[i][j])

    if not valid:
        break


# Check columns
if valid:
    for j in range(9):
        seen = set()

        for i in range(9):
            if board[i][j] == ".":
                continue

            if board[i][j] in seen:
                valid = False
                break

            seen.add(board[i][j])

        if not valid:
            break


# Check 3x3 boxes
if valid:
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):

            seen = set()

            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):

                    if board[i][j] == ".":
                        continue

                    if board[i][j] in seen:
                        valid = False
                        break

                    seen.add(board[i][j])

                if not valid:
                    break

            if not valid:
                break


print(valid)
