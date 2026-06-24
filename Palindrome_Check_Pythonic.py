# Program to check whether a given string is a palindrome by comparing it with its reverse.
s = input("Enter a string: ").strip().lower()

reversed_s = s[::-1]

if s == reversed_s:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is Not a Palindrome')
