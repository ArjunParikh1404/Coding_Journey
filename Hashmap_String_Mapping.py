# Given two strings, determine whether each character in the first string maps uniquely and consistently to a character in the second string.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 205

s1 = str(input("Enter the 1st string :"))

s2 = str(input("Enter the 2nd string :"))

hmap12 = {}
hmap21 = {}

if len(s1) != len(s2):
    print("False")
    
for i in range(len(s1)):
    if (s1[i] in hmap12 and hmap12[s1[i]] != s2[i]) or (s2[i] in hmap21 and hmap21[s2[i]] != s1[i]):
        print("False")
        break
    else:
        hmap12[s1[i]] = s2[i]
        hmap21[s2[i]] = s1[i]
else:
    print("True")
