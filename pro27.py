n,w=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
r=[]
c=0
for i in range(n):
    x=v[i]/p[i]
    r.append(x)
while w>=0 and len(r)>0:
    mindex=r.index(max(r))
    if w>=p[mindex]:
        c=c+v[mindex]
        w=w-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    r.pop(mindex)
print(c)
##
