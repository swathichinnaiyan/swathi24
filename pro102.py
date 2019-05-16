#square
n=input()
l1=[]
for i in range(0,len(n)):
    s=int(n[i])**2
    l1.append(s)
print(sum(l1))    
