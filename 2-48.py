#swa
n=int(input())
l=[]
for i in range(1,n+1):
	if n%i==0:
		if i%2!=0:
			l.append(i)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
		
