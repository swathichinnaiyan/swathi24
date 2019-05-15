#swa
s=input()
s=int(s)
l=[]
for i in range(0,s):
    s1=input()
    l.append(s1)
c=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        c.append(i[0])
    else:
        break
print(''.join(c))
