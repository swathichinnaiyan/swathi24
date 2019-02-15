#swa
n,k=map(int,input().split(" "))
count=0
for i in range(n,k+1):
    for j in range(2,i+1):
        if i%j==0:
            break
        
    if j==i:
        count=count+1
print(count)        
