data_1=list(range(1,32))
data_2=list(range(1,31))
data_3=list(range(1,30))
data_4=list(range(1,29))
month_1=(1,3,5,7,8,10,12)
month_2=(4,6,9,11)

while True:
    y,m,x=input().split()
    y,m,x=int(y),int(m),str(x)
    if not 1000<=y<=3000 and 1<=m<=12 and 0<=x<=9:
        pass
    elif m in month_1:
        counts= sum(str(day).count(str(x))for day in data_1) + 31
    elif m in month_2:
        counts= sum(str(day).count(str(x))for day in data_2) + 30
    elif m==2:
        if not y%400==0:
            counts= sum(str(day).count(str(x))for day in data_4) +28
        else:
            counts= sum(str(day).count(str(x))for day in data_3) +29
    print(counts)