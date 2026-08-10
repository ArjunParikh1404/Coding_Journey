# Check whether a given string is a palindrome after ignoring non-alphanumeric characters and case differences.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 125

s = input("Enter the string : ")

first = 0
last = len(s) - 1

while first < last:

    while first < last and not s[first].isalnum():
        first += 1

    while first < last and not s[last].isalnum():
        last -= 1

    if s[first].lower() != s[last].lower():
        print(False)
        break

    first += 1
    last -= 1

else:
    print(True)
