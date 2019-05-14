#swa
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(i+1,n):
        sum1=l[i]+l[j]
        if sum1==k:
            c=c+1
if c>=1:
    print("YES")
else:
    print("NO")
