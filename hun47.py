#swa
import re
n=input()
l=[]
r=re.sub(' +', ' ', n)
l.append((r.strip()))
for i in range(0,len(l)-1):
    print(l[i],end="")
print(l[-1])    
