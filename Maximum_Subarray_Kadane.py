# This program finds the largest possible sum from any continuous group of numbers in an array using Kadane's Algorithm.
# Maximum Subarray 

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")

for i in range(n):
    num = int(input())
    arr.append(num)

# Kadane's Algorithm
current_sum = arr[0]
max_sum = arr[0]

for i in range(1, n):

    current_sum = max(arr[i], current_sum + arr[i])

    max_sum = max(max_sum, current_sum)

print("\nArray:", arr)
print("Maximum Subarray Sum:", max_sum)
