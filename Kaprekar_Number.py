# Function to check if a number is Kaprekar

def is_kaprekar(n):
    if n < 1:
        return False

    square = n * n
    d = len(str(n))
    
    right = square % (10 ** d)
    left = square // (10 ** d)

    return right > 0 and (left + right == n)


num = int(input("Enter a number: "))

if is_kaprekar(num):
    print(num, "is a Kaprekar number")
    
else:
    print(num, "is not a Kaprekar number")
