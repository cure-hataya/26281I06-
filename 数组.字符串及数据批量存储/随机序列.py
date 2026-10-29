t_end =int(input())
t_start= 0
while t_start <= t_end:
	nums = list(map(int,input().split()))
	n = len(nums)
	avg =sum(nums)/n
	answer =sum((x - avg) ** 2 for x in nums) 
	print(max(nums) - min(nums), answer)
t_start +=1