#swa
s=int(input())
n=list(map(int,input().split(" ")))
count=0
for i in range(0,len(n)):
	for j in range(i+1,len(n)):
		count=count+1
print(count)		
