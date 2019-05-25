#swa
n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
l1=[]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]==s[j]:
            l1.append(j)
            
for i in range(len(l1)):
	l1[i]=l1[i]+1
print(*l1)
