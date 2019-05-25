#s
n=input()
l1=[]
for i in range(0,len(n)):
    if int(n[i])%2!=0:
        l1.append(n[i])
print(*l1)        
        
