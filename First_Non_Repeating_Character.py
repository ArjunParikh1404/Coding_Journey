# Find the First Non-Repeating Character by traversing the string and checking the frequency of each character using a HashMap.
# Time Complexity = O(n), Space Complexity = O(n)

s = input("Enter the String:")

ans = -1
d = {}

for ch in s:
    d[ch] = d.get(ch, 0) + 1

for ch in s:
    if d[ch] == 1:
        ans = ch
        break

print(ans)
