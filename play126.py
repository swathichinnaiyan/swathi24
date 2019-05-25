#sw
n,k=map(int,input().split())
l=list(map(int,input().split()))
g=[]
for i in l:
    if l.count(i)<k and i not in g:
        g.append(i)
a=sorted(g)
print(*a)
