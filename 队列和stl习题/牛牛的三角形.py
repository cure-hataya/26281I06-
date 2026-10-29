n = int(input())
ai =list(map(int,input().split()))
for i in range(n):
    if (ai[i])**2+ai[i+1]**2 >= ai[i+2]:
        print(ai[i] ,ai[i+1],ai[i+2])
        break
    else:
        print("No Solution")
