#swa
n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
k.sort()
c=0
j=1
for i in range(0,len(k)):
    p=l.count(k[i])
    c=c+p*j
    j=j+1
print(c)
