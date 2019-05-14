#swa
n=int(input())
l=list(map(int,input().split(" ")))
a=0
for i in range(0,len(l)-1):
    sum1=l[i]+l[i+1]
    a=a+sum1
print(a)    
    
