# Given a string s, return the index of the first non-repeating character, or -1 if none exists.
# Time Complexity = O(n), Space Complexity = O(n)

string = str(input("Enter the string :"))

hmap = {}

for ch in string:
    if ch in hmap:
        hmap[ch] += 1
    else:
        hmap[ch] = 1
        
for i,ch in enumerate(string):
    if hmap[ch] == 1:
        print(i)
        break
else:
    print("-1")
