# Given a string containing words separated by single spaces, reverse the characters of each word while keeping the word order and spaces unchanged.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 557

s = str(input("Enter the String :"))

s = s.split()

for i in range(len(s)):
    s[i] = s[i][::-1]
    
s = " ".join(s)

print(s)
