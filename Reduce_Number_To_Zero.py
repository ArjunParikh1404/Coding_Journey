# Reduce the number to zero by dividing even numbers by 2 and subtracting 1 from odd numbers, while counting the steps.

no = int(input("Enter the number"))

step = 0

while no != 0:
    if no % 2 == 0:
        no = no // 2
    else:
        no -= 1
    step += 1
        
print(f"It takes {step} time to reach zero")
