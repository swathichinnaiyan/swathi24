#s
n=int(input())
arr=list(map(int,input().split()))
p=1
op=[]
for i in arr:
  p=p*i
for i in arr:
  op.append(p//i)
print(*op)

