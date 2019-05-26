#s
n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
p=sorted(l1)
a=[]
for i in p:
    s=l1.index(i)
    a.append(l[s])
print(*a)
    
