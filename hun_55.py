#Swa
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
i=0
while k>0:
  l.append(l[i])
  del(l[i])
  k=k-1
print(*l)
