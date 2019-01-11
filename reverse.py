n=int(input())
r=0
l=[]
while n!=0:
	r=n%10
	n=n//10
	l.append(r)

for i in reversed(l):
  print(i,end=" ")
	
