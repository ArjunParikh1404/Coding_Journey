# Generate triangular numbers

no = int(input("Enter how many triangular numbers to generate: "))

total = 0

for i in range(1, no + 1):
    total += i
    print(total)
