import math
t =int(input())
s =str(t)
def sushu(t):
    if t < 2:
        return False
    if t%2==0:
        return t==2
    for i in range(3,int(math.isqrt(t))+ 1,2):
        if t% i ==0:
            return False
    return True
nums =list(s)
sorted_asc = sorted(s)
sorted_desc= sorted(s,reverse=True)
if nums == sorted_asc or nums ==sorted_desc:
    pal =s + s[-2::-1]
    p =int(pal)
    if sushu(p):
        print("prime")
    else:
        print("noprime")
else:
    print("noprime")
    
                
			  