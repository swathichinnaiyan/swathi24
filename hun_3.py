#swa
n=int(input())
l=[int(x) for x in input().split()]
x=[]
for i in range(0,len(l)):
    if i==l[i]:
        x.append(i)
print(*x)    
