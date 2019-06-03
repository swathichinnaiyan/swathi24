#swa
l,r,n=map(int,input().split())
c=0
n=str(n)
for i in range(l,r+1):
    s=str(i)
    if n in s:
        c+=1
print(c)
