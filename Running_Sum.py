# Running sum of 1D array

li = list(map(int, input("Enter the Numbers").split()))

for i in range(1, len(li)):
    li[i] += li[i - 1]

print (li)
