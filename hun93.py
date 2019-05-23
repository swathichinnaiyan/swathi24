#s
n=input()
l=[]
for i in range(0,len(n)):
    if i%2==0:
        l.append(n[i].upper())
    else:
        l.append(n[i])
print("".join(l))        
        
