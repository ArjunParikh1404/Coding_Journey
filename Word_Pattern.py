# Given a pattern and a string s, determine whether s follows the same pattern, where each character maps to exactly one unique word.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 290

pattern = input("Enter the pattern: ")

s = input("Enter the string: ")

words = s.split()

if len(pattern) != len(words):
    print(False)

else:
    char_to_word = {}
    word_to_char = {}

    result = True

    for i in range(len(pattern)):

        if pattern[i] in char_to_word:
            if char_to_word[pattern[i]] != words[i]:
                result = False
                break

        elif words[i] in word_to_char:
            result = False
            break

        else:
            char_to_word[pattern[i]] = words[i]
            word_to_char[words[i]] = pattern[i]

    print(result)
