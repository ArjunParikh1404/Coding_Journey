# Program to check whether a number is a Harshad Number

no = int(input("Enter the number"))

addition = sum(int(digit) for digit in str(no))

if addition == 0:
    print("Invalid input (sum of digits is 0)")
    
elif no%addition == 0:
    print("Number is Harshad Number")
    
else:
    print("Number is not Harshad Number")
