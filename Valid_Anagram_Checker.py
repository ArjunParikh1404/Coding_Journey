# This program checks whether two input strings are valid anagrams of each other.

def is_anagram(s, t):

    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # Check lengths
    if len(s) != len(t):
        return False

    # Count characters
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


# Dynamic Input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Check anagram
if is_anagram(str1, str2):
    print("Valid Anagram")
else:
    print("Not an Anagram")
