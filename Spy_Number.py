"""
Spy Number
Example:
Number = 1124
Sum of digits = 1 + 1 + 2 + 4 = 8
Product of digits = 1 * 1 * 2 * 4 = 8

Since the sum and product are equal, 1124 is a Spy Number.
"""

def is_spy_number(n):
    total_sum = 0
    total_product = 1

    while n > 0:
        digit = n % 10
        total_sum += digit
        total_product *= digit
        n //= 10

    return total_sum == total_product


num = int(input("Enter a number: "))

if is_spy_number(num):
    print("Given number is a Spy Number.")
else:
    print("Given number is not a Spy Number.")
