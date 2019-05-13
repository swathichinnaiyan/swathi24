#Swa
n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
	p=sum(l[i::2])
	if m<p:
		m=p
print(m)
