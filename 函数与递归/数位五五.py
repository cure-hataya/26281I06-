num_1 ,num_2= input().split()
num_1,num_2=int(num_1),int(num_2)
count=0
for nums in range(num_1,num_2+1):
    s = 0
    for ch in str(nums):
        s += int(ch)
    if s%5==0 :
        count+=1
print(count)
        