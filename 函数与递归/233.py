num =int(input())
run_end=0
nums=[]
while run_end <= num-1:
    a,b=input().split()
    a,b=int(a),int(b)
    answer = a * b
    nums.append(answer)
    run_end+=1
print(nums[:])