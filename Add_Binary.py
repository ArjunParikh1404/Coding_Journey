# Given two binary strings a and b, return their sum as a binary string without converting the inputs directly to decimal.
# Time Complexity = O(max(n, m)), Space Complexity = O(max(n, m))
# Leetcode = 67

a = str(input("Enter the a binary string :"))
b = str(input("Enter the b binary string :"))

carry = 0       
result = []     

i = len(a) - 1
j = len(b) - 1

while i >= 0 or j >= 0 or carry :
    total = carry
    
    if i >= 0:
        total += int(a[i])
        i -= 1
    
    if j >= 0:
        total += int(b[j])
        j -= 1
        
    result.append(str(total % 2))
    
    carry = total // 2
    
print("".join(result[::-1]))
