# Find the index of the first non-repeating character in a user-provided string.

from collections import Counter

def first_unique_char(s):
    count = Counter(s)

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1

text = input("Enter a string: ")

result = first_unique_char(text)

print("Index of first unique character:", result)
