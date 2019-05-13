#swa
n=int(input())
l=[int(x) for x in input().split()]
x=[]
for i in range(0,len(l)):
    if i==l[i]:
        x.append(i)
if len(x)==0:
    print(-1)
        
print(*x)
