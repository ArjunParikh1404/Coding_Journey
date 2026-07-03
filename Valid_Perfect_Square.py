# Given a positive integer num, return true if num is a perfect square or false otherwise.
# Time Complexity = O(1), Space Complexity = O(1)
# Leetcode = 367

num = int(input("Enter the number : "))

root = int(num ** 0.5) 

if root * root == num:
    print("True")
else:
    print("False")
