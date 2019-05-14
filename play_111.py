#swa
n,m=map(int,input().split())
li=list(map(int,input().split()))
lis=li[:n]
lis1=li[n:]
op=[]
for i in lis:
  for j in lis1:
    if i==j:
      op.append(i)
      lis1.pop(lis1.index(j))
      break
print(*sorted(op))
