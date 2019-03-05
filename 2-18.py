#swa
from collections import Counter
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
t=Counter('kabali')
a=t.values()
c=0
for i in l:
    x=Counter(i)
    b=x.values()
    if(sorted(list(a))==sorted(list(b))):
        c+=1
print(c)
