# Program to check if a number is a Disarium number.

def is_disarium(number):

    digits = str(number)
    total = 0
    
    for index, digit in enumerate(digits, start=1):
        total += int(digit) ** index
    
    return total == number

num = int(input("Enter a number: "))

if is_disarium(num):
    
    print(f"{num} is a Disarium number.")
    
else:
    
    print(f"{num} is not a Disarium number.")
