#s
n=int(input())
l=list(map(int,input().split()))
c=1
s=[]
for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
                c=c+1
        else:
               s.append(c)
               c=1
s.append(c)
print(max(s))
