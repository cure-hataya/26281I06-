n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_B = sum(B)
diff = [A[i] - B[i] for i in range(n)]
diff.sort(reverse=True)

ans = total_B + sum(diff[:K])
print(ans)
