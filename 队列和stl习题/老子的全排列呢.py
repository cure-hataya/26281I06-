import itertools

nums = [1, 2, 3, 4, 5, 6, 7, 8]
for p in itertools.permutations(nums):
    print(' '.join(map(str, p)))