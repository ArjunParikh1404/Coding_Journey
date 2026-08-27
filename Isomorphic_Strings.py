# Determine whether two strings are isomorphic by checking if each character in one string maps uniquely and consistently to a character in the other.
# Time complexity = O(n), Space complexity = O(1)
# Leetcode = 205

s = input("Enter the first string: ")
t = input("Enter the second string: ")

mapst = {}
mapts = {}

for i in range(len(s)):
    a = s[i]
    b = t[i]

    if (a in mapst and mapst[a] != b) or \
       (b in mapts and mapts[b] != a):
        print("False")
        break

    mapst[a] = b
    mapts[b] = a
else:
    print("True")
