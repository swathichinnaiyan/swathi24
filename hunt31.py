#swa
n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,n):
    c=1
    for j in range(i,n):
        c=c*l[j]
    a.append(c)
for i in range(0,n):
    c=1
    for j in range(i+1):
        c=c*l[j]
    a.append(c)
print(max(a))
