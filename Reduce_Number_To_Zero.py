# Reduce the number to zero by dividing even numbers by 2 and subtracting 1 from odd numbers, while counting the steps.

no = int(input("Enter the number"))

i = 0

while True:
    if no == 0:
        break
    elif no % 2 == 0:
        no = no // 2
        i += 1
    else:
        no -= 1
        i += 1
        
print(f"It takes {i} time to reach zero")
