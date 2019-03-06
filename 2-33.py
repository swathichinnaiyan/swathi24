#swa
n=input()
l=[]
for i in range(0,len(n)):
	if i==0 or i==3:
		l.append(n[i])
for i in range(0,len(l)-1):
	print(l[i],end="")
print(l[-1])	
		
		
