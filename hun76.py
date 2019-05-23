#swa
n=int(input())
k=[]
q=[]
for i in range(n):
    l=list(map(int,input().split()))
    k.append(l)
   
for i in k:
    q.append(sum(i))
    
b=sum(q)/(n*n)

print("%.6f" %b)
