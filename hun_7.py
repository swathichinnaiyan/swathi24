#Swa
n=int(input())
l=[int(x) for x in input().split()]
l1=[]

for i in range(0,len(l)):
    if  i %2!=0 and l[i]%2==0:
        l1.insert(i,l[i])
    elif i%2==0 and l[i]%2!=0:
        l1.insert(i,l[i])

print(*l1)
