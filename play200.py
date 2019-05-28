n=input()
l=[]
for i in range(0,len(n)):
    if n[i] not in l:
        l.append(n[i])
print(*l)        
#
