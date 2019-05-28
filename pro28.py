#
n=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
c=0
for i in range(len(l)):
    if l[i]>=s:
        c=c+1
    s=s+l[i]
print(c)
