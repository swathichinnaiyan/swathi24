#swa
n=int(input())
l=list(map(int,input().split()))
s=0
lis=[]
for i in range(0,n):
    s=s+l[i]
    lis.append(s)
print(*lis[::-1])    
