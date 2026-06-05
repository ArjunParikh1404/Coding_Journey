# This program checks each number in a list and prints whether it has an even or odd number of digits

nums = list(map(int, input("Enter the array: ").split()))

for num in nums:
    digit_count = len(str(abs(num))) 

    if digit_count % 2 == 0:
        print(f"{num} Number is even")
    else:
        print(f"{num} Number is odd")
