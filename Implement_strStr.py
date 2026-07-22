# Given two strings haystack and needle, return the starting index of the first occurrence of needle in haystack; return -1 if it does not occur.
# Time Complexity = O(n × m), Space Complexity = O(1)
# Leetcode = 28

haystack = str(input("Enter the haystack string:"))
needle = str(input("Enter the needle string:"))

i = 0

while i <= len(haystack) - len(needle):
    if haystack[i] == needle[0]: 
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
        else:
            print(i)
            break
    
    i += 1

else:
    print("-1")
