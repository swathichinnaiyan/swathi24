#w
n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    m=(n-1)//2
    a=sorted(l[0:m])
    b=sorted(l[m:])
    s=a+b[::-1]
    print(*s)
else:
    m=n//2
    a=sorted(l[0:m])
    b=sorted(l[m:])
    s=a+b[::-1]
    print(*s)
