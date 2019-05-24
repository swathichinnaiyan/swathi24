#sw
n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if i<0:
        c=c+i
print(c)        
        
