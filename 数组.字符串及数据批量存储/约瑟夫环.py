n,k,m =input().split()
n,k,m = int(n),int(k),int(m)
n_list= list(range(n))
while len(n_list)>1:
    k = (k + m - 1)%len(n_list)
    n_list.pop(k)
print(n_list[0])
            
        