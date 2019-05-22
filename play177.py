#swa
l=list(input().split())
l1=[]

for i in l:
  l1.append(sorted(list(i)))
op=[]
for i in l1:
  op.append("".join(i))
print(*op)
