#s
n=input()
l=[]
for i in range(0,len(n)):
    if n[i] not in l:
        l.append(n[i])
l=l[::-1]
for i in range(0,len(l)-1):
    print(l[i],end="")
print(l[-1])    
