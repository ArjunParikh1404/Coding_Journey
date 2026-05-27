# Move all zeros to the end while maintaining the order of non-zero elements

def move_zeros(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums

arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("Output:", move_zeros(arr))
