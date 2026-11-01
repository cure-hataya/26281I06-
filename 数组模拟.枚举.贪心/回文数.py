cnt = list(map(int, input().split()))

odd = 0
mid = -1
for i in range(10):
    if cnt[i] % 2 == 1:
        odd += 1
        mid = i

if odd > 1:
    print(-1)
else:
    left = []
    for i in range(10):
        left.extend([str(i)] * (cnt[i] // 2))

    if len(left) > 0 and left[0] == '0':
        for i in range(1, 10):
            if cnt[i] > 0:
                left[0], left[i // 1] = left[i // 1], left[0]
                break
        else:
            print(-1)
            raise SystemExit

    if len(left) > 0 and left[0] == '0':
        print(-1)
    else:
        s = ''.join(left)
        if mid != -1:
            s = s + str(mid) + s[::-1]
        else:
            s = s + s[::-1]
        if s[0] == '0' and len(s) > 1:
            print(-1)
        else:
            print(s)