#sw
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n+1):
    if l.count(i)!=1:
        break
if i==n and l[-1]>n:
    print("no")
elif i==n and l[-1]<=n:
    print("yes")
else:
    print("no")
