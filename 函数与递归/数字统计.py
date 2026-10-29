counts = 0
a,b =input().split()
a,b = int(a),int(b)
for nums in range(a-1,b+1,1):
	if str(2) in str(nums) :
		times = str(nums).count(str(2))
		counts += int(times)
print(counts)