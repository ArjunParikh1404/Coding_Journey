# Check whether a string of brackets (), [], {} is properly balanced using a stack.

def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Dynamic Input
s = input("Enter parentheses string: ")

if is_valid(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")
