counts = 0
a, b = input().split()
a = int(a)
b = str(b)
for nums in range(0, a + 1):
    if str(b) in str(nums):
        counts += str(nums).count(str(b))
print(counts)
