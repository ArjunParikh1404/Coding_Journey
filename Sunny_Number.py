# Program to check whether a given number is a Sunny Number.
# A number is Sunny if (n + 1) is a perfect square.

import math

n = int(input("Enter a number: "))

if n < 0:
    print("Sunny numbers are non-negative only.")
else:
    root = math.isqrt(n + 1)   # integer square root
    
    if root * root == n + 1:
        print(n, "is a Sunny Number")
    else:
        print(n, "is NOT a Sunny Number")
