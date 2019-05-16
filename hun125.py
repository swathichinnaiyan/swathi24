3swa
s=input()
l1=[]
for i in s:
    if s.count(i)==1:
        l1.append(i)
for i in range(0,len(l1)-1):
    print(l1[i],end="")
print(l1[-1])    
