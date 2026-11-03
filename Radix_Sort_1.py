# Radix Sort 
# Time Complexity = O(d×(n+10)), Space Complexity = O(n+10)

def radixSort(nums):
    max_num = max(nums)
    exp = 1

    while max_num // exp > 0:
        output = [0] * len(nums)
        count = [0] * 10

        for num in nums:
            index = (num // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for num in reversed(nums):
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1

        nums = output
        exp *= 10

    return nums

nums = list(map(int, input("Enter the list:").split()))

print(radixSort(nums))
