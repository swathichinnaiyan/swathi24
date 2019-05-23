#swa
n,k=map(int,input().split(" "))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(0,len(b)):
	if b[i] in a:
		c+=1
if len(b)==c:
	print("YES")
else:
	print("NO")
