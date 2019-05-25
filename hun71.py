#sw
n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(n-k,n):
    l1.append(l[i])
print(*l1)    
