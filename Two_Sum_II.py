# Given a sorted array of integers and a target value, find the two numbers that add up to the target and return their 1-based indices using constant extra space.
# Time Complexity = O(n), Space Complexity = O(n), Auxiliary Space = O(1)
# Leetcode = 167

numbers = list(map(int, input("Enter the list of numbers : ").split()))
target = int(input("Enter the target : "))
result = []

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]
    
    if total == target:
        result.append(left + 1)
        result.append(right + 1)
        break
    elif total < target:
        left += 1
    else:
        right -= 1
        
print(result)
