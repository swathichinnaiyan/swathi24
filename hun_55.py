#swa
n,k=map(int,input().split(" "))
l=[int(i) for i in input().split()]
i=0
while n>0:
    l.append(l[i])
    del(l[i])
    k=k-1
    break
print(*l)
