# Array Contains Duplicate ?

nums = list(map(int, input("Enter array elements separated by space: ").split()))

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("\nArray:", nums)

if duplicates:
    print("Contains Duplicate: True")
    print("Duplicate Numbers:", list(duplicates))
else:
    print("Contains Duplicate: False")
