n=int(input())

a=0
b=1
i=1
l=[]
while i<=n:
  
  c=a+b
  a=b
  b=c
  
	
  i=i+1
  l.append(a)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
