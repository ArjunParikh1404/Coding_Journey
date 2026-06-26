# Program to convert time from minutes into hours and minutes

minutes = int(input("Enter time in minutes: "))

hours, minutes = divmod(minutes, 60)

print(f"{hours} hour(s) and {minutes} minute(s)")
