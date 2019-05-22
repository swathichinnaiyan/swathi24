#Swa
n,k=input().split()
k=int(k)
l=[]
for i in range(k-1,len(n),k):
    l.append(n[i])
print(*l)    
