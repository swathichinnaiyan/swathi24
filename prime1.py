n,k=map(int,input().split(" "))
n=n+1
l=[]
for n in range(n,k):
    i1=2
    while i1<n:
        if n%i1==0:
            break
        i1=i1+1
    if n==i1:
        l.append(n)
  
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1])  
