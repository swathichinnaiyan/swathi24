#swathi
n,k=map(int,input().split(" "))
l=[]
for n in range(n+1,k):
    x=n
    amn=0
    while n>0:
        r=n%10
        amn=amn+r**3
        n=n//10
    if x==amn:
        l.append(x)
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1])  
