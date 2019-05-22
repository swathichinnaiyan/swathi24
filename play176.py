#sa
a,b=map(str,input().split())
l1=list(set(list(a)))
l2=list(set(list(b)))
l1.sort()
l2.sort()
if l1==l2:
    print("true")
else:
    print("false")
