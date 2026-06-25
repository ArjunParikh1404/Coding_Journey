# Program to check balanced parentheses in a string (Bracket matcher)

def is_balanced(s):
    count = 0

    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0


# Dynamic input
s = input("Enter a string: ")

# Output
if is_balanced(s):
    print("Balanced")
else:
    print("Not Balanced")
