# Program to Check Whether a Number is a Neon Number
# 1 , 9

no = int(input("Enter the number"))

square = no * no

total = sum(int(digit) for digit in str(square))

if total == no:
    print("Number is a Neon number")

else:
    print("Number is not a Neon number")
