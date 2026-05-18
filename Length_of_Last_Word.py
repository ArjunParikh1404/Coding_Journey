# Length of Last Word

s = input("Enter a string: ").strip()

words = s.split()

if words:
    print("Length of last word:", len(words[-1]))
else:
    print("No words found")
