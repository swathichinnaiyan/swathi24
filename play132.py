n=input()
l=[]
c=0
for i in range(0,len(n)-1):
    k=int(n[i])+int(n[i+1])
    if k%2!=0:
        c+=1
    else:
        l.append(c)
        c=0
    l.append(c)
m=max(l)
if m==0:
    print(0)
else:
    print(m+1)
    #odd
