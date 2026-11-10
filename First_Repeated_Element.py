# Find the First Repeated Element by traversing the array and checking whether an element already exists in the HashSet.
# Time Complexity = O(n), Space Complexity = O(n)

arr = list(map(int, input("Enter the Array:").split()))

ans = -1
s = set()

for n in arr:
    if n in s:
        ans = n
        break

    s.add(n)

print(ans)
