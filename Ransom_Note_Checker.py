# Check whether the ransom note can be formed using characters from the magazine.

ransomNote = input("Enter the ransomNote: ")
magazine = input("Enter the magazine: ")

li = []

for i in magazine:
    li.append(i)
    
for j in ransomNote:
    if j not in li:
        print("False")
        break
    
else:
    print("True")
