# Determine whether a number is a Happy Number by repeatedly replacing it with the sum of the squares of its digits until it reaches 1 or enters a cycle.
# Time Complexity = O(log n), Space Complexity = O(log n)
# Leetcode = 202

n = int(input("Enter the Number :"))

ans = False
s = set()

while n not in s:
    s.add(n)
    total = 0
    
    while n != 0:
        ones = n % 10
        n = n // 10
        
        total += ones**2
        
    n = total
    
    if n == 1:
        ans = True
        break
    
print(ans)
