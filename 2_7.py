#swa
s=input()
l=list(s)

for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print(''.join(l))
