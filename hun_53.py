#swa
n,k=map(str,input().split())
k=int(k)
d=[]
for i in range(0,len(n)-k+1):
	d.append(n[i:i+k])
print(*d)
