# Divide two integers without using multiplication, division, or modulo operators, truncating the result toward zero.
# Time Complexity = O(log² n), Space Complexity = O(1)
# Leetcode = 29

INT_MAX = 2**31 - 1
INT_MIN = -2**31

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

if dividend == INT_MIN and divisor == -1:
    print(INT_MAX)

else:
    negative = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        temp = divisor
        multiple = 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        quotient += multiple

    if negative:
        quotient = -quotient

    print(quotient)
