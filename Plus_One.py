# Given an array of digits representing a number, add 1 to the number and return the updated digit array.
# Time Complexity = O(n), Space Complexity = O(1)
# leetcode = 66

digits = list(map(int,input("Enter the array :").split()))

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        print(digits)
        break
    digits[i] = 0
else:
    digits = [1] + digits
    print(digits)
