# Converts a Roman numeral entered by the user into its equivalent integer value.

def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]

    return total


while True:
    roman_number = input("Enter a Roman numeral (or Q to quit): ").upper()

    if roman_number == "Q":
        print("Goodbye!")
        break

    result = roman_to_int(roman_number)

    print("Integer value:", result)
    print()
