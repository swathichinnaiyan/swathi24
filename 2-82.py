#swa
n=int(input())
l=list(map(int,input().split(" ")))
s=l[0]
for i in range(0,len(l)):
	c=s&l[i]
print(c)	
