# Program to check whether a given number is a Trimorphic number.
# A Trimorphic number is a number whose cube ends with the number itself.

n = int(input("Enter a number: "))

digits = len(str(n))

if (n * n * n - n) % (10 ** digits) == 0:
    print("Trimorphic number")
else:
    print("Not a trimorphic number")
