n=int(input())
sum1=0
n1=list(map(int,input().split(" ")))
for i in range(0,len(n1)):
	sum1=n1[i]+sum1
print(sum1//n)	
	
