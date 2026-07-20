# Given numRows, generate the first numRows rows of Pascal's Triangle where each element is the sum of the two numbers directly above it.
# Time Complexity = O(n²), Space Complexity = O(n²), Auxiliary Space = O(n)
# Leetcode = 118

numRows = int(input("Enter the number of row :"))

result = []
temp = []

for i in range(numRows):
    final = []
    for j in range(i):
        if j == 0:
            final.append(1)
        else:
            final.append(temp[j-1]+temp[j])
    
    final.append(1)
    result.append(final)
    temp = final

print(result)
