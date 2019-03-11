n=input()
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]<l[j]:
            c=c+1
print(c)
#sswa
