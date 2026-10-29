n, t = input().split()
n, t = int(n), int(t)
qdgg = list(input().strip())

t_end = 0
dot = qdgg.index('.')

while t_end < t:

    pos = -1
    for j in range(dot + 1, len(qdgg)):
        if qdgg[j] >= '5':
            pos = j
            break

    if pos == -1:
        break


    k = pos - 1
    while k >= 0:
        if qdgg[k] == '.':
            k -= 1
            continue
        if qdgg[k] == '9':
            qdgg[k] = '0'
            k -= 1
        else:
            qdgg[k] = str(int(qdgg[k]) + 1)
            break
    else:

        qdgg.insert(0, '1')


    del qdgg[pos:]


    if '.' in qdgg:
        dot = qdgg.index('.')
    else:
        break

    t_end += 1


while qdgg and qdgg[-1] == '0':
    qdgg.pop()

if qdgg and qdgg[-1] == '.':
    qdgg.pop()

print(''.join(qdgg))
