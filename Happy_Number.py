# Check if number is a Happy Number.

def happy(n): 
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1


number = int(input("Enter a number: "))

if happy(number):
    print(f"{number} is a Happy Number")
else:
    print(f"{number} is NOT a Happy Number")
