#swa
n=int(input())
l=[]
s=""
for i in input().split():
  l.append(i)
  s=s+min(l)+" "
print(s.strip())

