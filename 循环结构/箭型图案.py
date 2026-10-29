n = int(input())
for i in range(n+1):
    print(" "*(2*n-2*i)+"*"*(i+1))
    
for i in range(n,0,-1):
	print(" "*(2*n-2*(i-1))+"*"*(i))
                    