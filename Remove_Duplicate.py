# Remove duplicate numbers from a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)
        
print(unique)
