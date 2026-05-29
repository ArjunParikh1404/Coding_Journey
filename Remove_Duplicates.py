# This program takes user input, removes duplicate values using set(), and prints the unique elements.

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique = list(set(arr))

print("Unique elements:", unique)
