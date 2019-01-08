x, y = map(int, input().split())
l=[]
for i in range(x+1,y):
	if i%2!=0:
		l.append(i)
for i in range(len(l)-1):
	print(l[i],end=" ")
print(l[-1])		
