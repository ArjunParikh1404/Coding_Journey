# Program to check whether a given number is a Duck Number.
# A Duck Number is a number that contains at least one 0 but does not start with 0.

num = input("Enter the number: ").strip()

if num and '0' in num and not num.startswith('0'):
    print("Number is a Duck Number")
else:
    print("Number is not a Duck Number")
