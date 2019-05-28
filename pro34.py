#
n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
    l.append(input())
for i in range(n):
    for j in range(k-1):
        if l[i][j]=="R" and l[i][j+1]=="R":
            c=c+5
        elif l[i][j]=="G" and l[i][j+1]=="G":
            c=c+3
print(c)
