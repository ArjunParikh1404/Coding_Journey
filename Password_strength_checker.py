# Password Strength Checker
import re

def check_pass(passwd):
    
    score = 0

    # Conditions to check
    checks = [
        len(passwd) >= 8,
        re.search(r"[A-Z]", passwd),
        re.search(r"[a-z]", passwd),
        re.search(r"\d", passwd),
        re.search(r"[!@#$%^&*()_,.?\":{}|<>]", passwd)
    ]

    # Calculate score
    for check in checks:
        if check:
            score += 1

    # Determine strength
    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"


# User input
password = input("Enter the Password: ")

strength = check_pass(password)

print("Password Strength:", strength)
