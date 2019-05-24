#s
n=int(input())
k=[]
s=0
for i in range(n):
    l=list(map(int,input().split()))
    k.append(l)
j=n-1
for i in range(n):
    s=s+k[i][j]
    j=j-1
print(s)
