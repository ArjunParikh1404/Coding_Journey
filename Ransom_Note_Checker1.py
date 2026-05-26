# Check whether the ransom note can be formed using characters from the magazine.

ransomNote = input("Enter the ransomNote: ")
magazine = input("Enter the magazine: ")

count = {}

for ch in magazine:
    count[ch] = count.get(ch, 0) + 1

for ch in ransomNote:
    if count.get(ch, 0) == 0:
        print("False")
        break
    count[ch] -= 1
else:
    print("True")
