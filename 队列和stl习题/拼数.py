n = int(input())
nums = input().split()
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

print(''.join(nums))