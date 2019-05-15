#swa
n=input()
l=list(n)
l1=[]
for i in range(0,len(n)):
    s=int(n[i])**i
    l1.append(s)
print(sum(l1))    
