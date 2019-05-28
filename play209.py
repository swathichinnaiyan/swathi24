#
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=1
k=1
j=n-1
for i in range(n):
    s=s*l[i][i]
    k=k*l[i][j]
    j=j-1
print(s+k)
