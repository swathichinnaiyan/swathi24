#swa
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=0
s=""
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            s=s+str(a[i])+" "
            b.remove(b[j])
            break
print(s.strip())
