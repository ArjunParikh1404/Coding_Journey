# Find all starting indices of p's anagrams in s.
# Time Complexity = O(n), Space Complexity = O(1)  (26 characters)

s = input("Enter the string : ")
p = input("Enter the pattern : ")

hmap = {}
count = [0] * 26

for ch in p:
    count[ord(ch) - ord('a')] += 1

hmap[tuple(count)] = 1

window = [0] * 26
result = []

for i in range(len(s)):

    window[ord(s[i]) - ord('a')] += 1

    if i >= len(p):
        window[ord(s[i - len(p)]) - ord('a')] -= 1

    if i >= len(p) - 1:
        if tuple(window) in hmap:
            result.append(i - len(p) + 1)

print(result)
