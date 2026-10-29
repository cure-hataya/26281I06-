l, m = input().split()
l, m = int(l), int(m)
tree_total = l + 1
time = 0
caculate = set()
while time < m:
    li, ri = list(map(int, input().split()))
    for i in range(li, ri + 1):
        caculate.add(i)
    time += 1
print(tree_total - len(caculate))
