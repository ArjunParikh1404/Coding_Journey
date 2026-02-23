def is_duck_number(num: int) -> bool:
    num_str = str(num)
    return '0' in num_str and not num_str.startswith('0')

# Example usage
number = int(input("Enter a number: "))
if is_duck_number(number):
    print("Duck Number")
else:
    print("Not a Duck Number")
