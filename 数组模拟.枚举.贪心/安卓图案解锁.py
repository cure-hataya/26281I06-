while True:
    try:
        passwd = input().strip()
    except EOFError:
        break
    if passwd == "":
        continue

    used = [False] * 10

    ok = True

    for i in range(len(passwd) - 1):
        cur = int(passwd[i])
        nxt = int(passwd[i + 1])

        if used[nxt]:
            ok = False
            break

        mid = 0
        if (cur == 1 and nxt == 3) or (cur == 3 and nxt == 1):
            mid = 2
        elif (cur == 1 and nxt == 7) or (cur == 7 and nxt == 1):
            mid = 4
        elif (cur == 1 and nxt == 9) or (cur == 9 and nxt == 1):
            mid = 5
        elif (cur == 2 and nxt == 8) or (cur == 8 and nxt == 2):
            mid = 5
        elif (cur == 3 and nxt == 7) or (cur == 7 and nxt == 3):
            mid = 5
        elif (cur == 3 and nxt == 9) or (cur == 9 and nxt == 3):
            mid = 6
        elif (cur == 4 and nxt == 6) or (cur == 6 and nxt == 4):
            mid = 5
        elif (cur == 7 and nxt == 9) or (cur == 9 and nxt == 7):
            mid = 8

        if mid != 0 and not used[mid]:
            ok = False
            break
        used[cur] = True
    if ok:
        print("YES")
    else:
        print("NO")





