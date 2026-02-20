# Program to check whether a number is an Abundant number

no = int(input("Enter the number"))

divisors = []

for i in range(1, no):
    if no % i == 0:
        divisors.append(i)
        
total = sum(divisors)

if total > no:
    print("Number is an Abundant number")
    
else:
    print("Number is not an Abundant number")
