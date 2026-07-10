# Write a program to count the number of 'a' or 'A' characters in a given string.
# Time Complexity = O(n), Space Complexity = O(1)

string = input("Enter the String: ")

count = 0

for char in string:
    if char.lower() == 'a':
        count += 1

print("Number of 'a' or 'A' characters:", count)
