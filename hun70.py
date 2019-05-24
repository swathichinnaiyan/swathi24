n,k,t=map(int,input().split())
c=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        s=l[i]+l[j]
        if s==t:
            c=c+1
            
            
if c>=1:
    print("YES")
else:
    print("NO")
           
