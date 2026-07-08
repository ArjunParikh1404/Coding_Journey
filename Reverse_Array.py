# Write a program to reverse the order of elements in a given array (or list of strings)
# Time Complexity = O(n), Space Complexity = O(1)

string = list(map(str, input("Enter the Array : ").split()))

left = 0
right = len(string) - 1

while left < right:
    string[left], string[right] = string[right], string[left]
    left += 1
    right -= 1

print(string)
