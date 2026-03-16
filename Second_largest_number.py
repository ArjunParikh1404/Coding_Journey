# This code is finding the second largest number

def second_largest(numbers):
    if len(numbers) < 2:
        return None  

    largest = numbers[0]
    second = None

    for num in numbers[1:]:
        if num > largest:
            second = largest
            largest = num
        elif second is None or (num > second and num != largest):
            second = num

    return second

user_input = input("Enter numbers separated by spaces: ")

numbers_list = [int(x) for x in user_input.split()]

result = second_largest(numbers_list)

if result is not None:
    print("Second largest number is:", result)
else:
    print("There is no second largest number.")
