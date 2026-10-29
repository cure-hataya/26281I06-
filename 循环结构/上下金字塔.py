
n = int(input())
for n_wide_1 in range(1,n+1):
    print(" "*( n - n_wide_1 ) + (2*n_wide_1-1)*"*")
for n_wide_1 in range(n-1,0,-1):
    print(" "*( n - n_wide_1 ) + (2*n_wide_1-1)*"*")
	