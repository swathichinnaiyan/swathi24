#swa
n=int(input())
l=list(map(int,input().split()))
s=""
for i in range(0,len(l)):
        if l[i]<n:
                s=s+str(l[i])+" "
print(s.strip())
