# Program to check whether a given number is a Pronic Number.
# A Pronic Number is a number that can be expressed as n * (n + 1),
# Example: 6 = 2 × 3, 12 = 3 × 4

n = int(input("Enter a number: "))

is_pronic = False
i = 0

while i * (i + 1) <= n:
    if i * (i + 1) == n:
        is_pronic = True
        break
    i += 1

if is_pronic:
    print("Pronic Number")
else:
    print("Not a Pronic Number")
