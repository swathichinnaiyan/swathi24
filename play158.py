#s
m,n=map(int,input().split())
p=m*n
c=bin(p)[2:]
a=0
#print(c)
for i in range(len(c)):
	if c[i]=="1":
	    a=a+1
	if a==2:
	    print(i+1)
	    break
		
