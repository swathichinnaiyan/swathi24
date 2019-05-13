#swa
n=int(input())
l=[int(x) for x in input().split()]
l1=[]
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l1.append(l[i])
            
for  i in range(0,len(l1)-1):
    c=c+1
    print(l1[0])
if c==0:
    print("unique")
    
