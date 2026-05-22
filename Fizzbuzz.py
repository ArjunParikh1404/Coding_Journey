# Print numbers from 1 to N, replacing multiples of 3 with "Fizz", 5 with "Buzz", and both with "FizzBuzz".

no = int(input("Enter the number :"))

for i in range(1, no+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
