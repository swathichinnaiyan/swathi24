#swa
n,k=map(str,input().split())
l=[]
l1=[]
for i in range(0,len(n)):
    for j in range(0,len(k)):
        if n[i]==k[j]:
            l.append(n[i])
           
for i in range(0,len(l)):
    if l[i] not in l1:
        l1.append(l[i])
for i in range(0,len(l1)-1):
    print(l1[i],end="")
print(l1[-1])    
            
