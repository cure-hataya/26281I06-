import sys

s = sys.stdin.read()
res = ""
i = 0
n = len(s)
in_str = False
in_comment = False
escape = False

while i < n:
    if in_str:
        if escape:
            res += s[i]
            escape = False
        elif s[i] == '\\':
            res += s[i]
            escape = True
        elif s[i] == '"':
            res += s[i]
            in_str = False
        else:
            res += s[i]
    elif in_comment:
        if i + 1 < n and s[i] == '*' and s[i + 1] == '/':
            in_comment = False
            i += 1
    else:
        if s[i] == '"':
            res += s[i]
            in_str = True
        elif i + 1 < n and s[i] == '/' and s[i + 1] == '*':
            in_comment = True
            i += 1
        else:
            res += s[i]
    i += 1

print(res, end="")