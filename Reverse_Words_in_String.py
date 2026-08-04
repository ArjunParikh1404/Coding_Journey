# Given a string, reverse the order of its words while removing extra spaces and ensuring exactly one space separates each word.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 151

s = str(input("Enter the string here :"))

s = s.split()

s = s[::-1]

s = " ".join(s)

print(s)
