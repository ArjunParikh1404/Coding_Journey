# Program to find the largest and smallest numbers in an array.

nums = list(map(int,input("Enter the Array : ").split()))

largest = max(nums)
smallest = min(nums)

print("Largest:", largest)
print("Smallest:", smallest)
