#a
n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in l:
    if i<=k:
        count=count+1
print(count)        
