#swa
n=int(input())
c=0
for i in range(n+1):
    k=str(i)
    if all(abs(int(k[j])-int(k[j-1]))==1 for j in range(1,len(k))):
        c=c+1
print(c)
