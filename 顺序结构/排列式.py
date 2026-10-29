results=[]
for a in range(1,100):
    for b in range(1,10):
        		c = a * b
s = str(a) + str(b) + str(c)
if len(s) == 9 and '0' not in s and sorted (s) == ['1','2','3','4','5','6','7','8','9']:
	results.append((c,a,b))
	results.sort()
	for item in results:
    	 	print(str(item[0]) + "=" + str(item[2]) + "x" + str(item[1]))