#swa
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l.sort()
l1=[]
for i in range(0,len(l)):
     if l[i]<k:
        l1.append(l[i])
for i in range(0,len(l1)-1):
     print(l1[i],end=" ")
print(l1[-1])
