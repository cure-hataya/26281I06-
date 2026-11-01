import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    T = int(lines[0])
    words = ["zero", "two", "four", "six", "nine"]
    nums = ["0", "2", "4", "6", "9"]
    out = []
    for i in range(1, T + 1):
        s = lines[i]
        ans = ""
        j = 0
        while j < len(s):
            if s[j] in "02469":
                ans += s[j]
                j += 1
            elif s[j] == 'z':
                ans += "0"
                j += 4
            elif s[j] == 't':
                ans += "2"
                j += 3
            elif s[j] == 'f':
                ans += "4"
                j += 4
            elif s[j] == 's':
                ans += "6"
                j += 3
            elif s[j] == 'n':
                ans += "9"
                j += 4
            else:
                j += 1
        out.append(ans)
    print("\n".join(out))

solve()