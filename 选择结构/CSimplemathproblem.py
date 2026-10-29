x,y = input().split()
x,y = int(x),int(y)
if y % x == 0 :
    print(x+y)
else:
    print(y-x)