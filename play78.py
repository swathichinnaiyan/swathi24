#
n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=l1+l2
s=sorted(s)
print(*s)
