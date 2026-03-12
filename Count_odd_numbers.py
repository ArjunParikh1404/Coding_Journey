# Program to count odd numbers from list

numbers = map(int, input("Enter numbers separated by space: ").split())

count = sum(1 for i in numbers if i % 2 != 0)

print(count)
