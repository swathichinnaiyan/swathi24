#s
s,m=map(str,input().split())
if len(s)==len(m):
    a=s
    b=m
else:
    if len(s)>len(m):
        a=s[:len(m)]
        b=m
    else:
        a=m[:len(s)]
        b=s
    
print(a+b)
