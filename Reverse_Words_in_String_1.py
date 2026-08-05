# Given a string, reverse the order of its words while removing extra spaces and ensuring exactly one space separates each word.
# Time Complexity = O(n), Space Complexity = O(1)
# Leetcode = 151

s = str(input("Enter the string here :"))

s = s.split()

first = 0
last = len(s) - 1

while first < last:
    s[first], s[last] = s[last], s[first]
    first += 1
    last -= 1
    
s = " ".join(s)

print(s)
