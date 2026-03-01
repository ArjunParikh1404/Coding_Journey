# Program to check whether a given number is an Emirp number.
# An Emirp number is a prime number that becomes a different prime number when its digits are reversed.

import math

def is_prime(n: int) -> bool:
    """Checks if a number is a prime number."""
    if n <= 1:
        return False
    # Check divisibility up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n: int) -> int:
    """Returns the reverse of a number, ignoring leading zeros in reverse."""
    reversed_num = 0
    temp = abs(n)
    while temp != 0:
        unit_digit = temp % 10
        reversed_num = reversed_num * 10 + unit_digit
        temp //= 10
    # Restore the sign for negative numbers if necessary
    return int(math.copysign(reversed_num, n))

def is_emirp(number: int) -> bool:
    """Checks if a number is an emirp number."""
    if not is_prime(number):
        return False
        
    reversed_num = reverse_number(number)
    
    if number == reversed_num:
        return False
        
    if not is_prime(reversed_num):
        return False
        
    return True

# Take number from the user
num = int(input("Enter a number: "))

if is_emirp(num):
    print(f"{num} is an emirp number.")
else:
    print(f"{num} is not an emirp number.")
