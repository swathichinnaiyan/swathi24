#swa
n=int(input())
l=list(map(int,input().split()))
m=min(l)
s=l.index(m)
n=max(l)
n1=l.index(n)
print(n1-s)
