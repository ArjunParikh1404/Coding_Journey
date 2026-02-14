# Check if number is Automorphic

no = int(input("Enter the number: "))

square = no * no

if str(square).endswith(str(no)):
    print("Number is Automorphic number")
    
else: 
    print("Number is not Automorphic number")
