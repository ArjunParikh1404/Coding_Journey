# Determine whether two strings are isomorphic by checking if each character in one string maps uniquely and consistently to a character in the other.
# Time complexity = O(n), Space complexity = O(n)
# Leetcode = 205

s = str(input("Enter the first string :"))
t = str(input("Enter the second string :"))
mapst = {}
mapts = {}

if len(s) != len(t):
    print("False")

else:
    for i in range(len(s)):
        mapst[s[i]] = t[i]
        mapts[t[i]] = s[i]
        
    for j in range(len(s)):
        if t[j] != mapst[s[j]] or s[j] != mapts[t[j]]:
            print("False")
            break
    else:
        print("True")
