#w
a,b,c=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in l:
    if i>=b and i<=c:
        print(i)
        break
