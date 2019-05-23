#swa
a=input().split()
s=[]
for i in range(0,len(a)):
    if i%2==0:
        s.append(a[i][::-1])
    else:
        s.append(a[i])
print(" ".join(s))        
