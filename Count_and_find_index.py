# This program is about counts how many times a specific number appears in a list and finds the index of its first occurrence.

nums = [1, 2, 2, 3, 4, 2, 5]

value_to_check = int(input("Enter a number to check in the list: "))

# Count occurrences

count_value = nums.count(value_to_check)

print(f"{value_to_check} occurs {count_value} time(s) in the list.")

# Find index of first occurrence

if value_to_check in nums:
    
    first_index = nums.index(value_to_check)
    
    print(f"The first occurrence of {value_to_check} is at index {first_index}.")
    
else:
    
    print(f"{value_to_check} is not in the list.")
