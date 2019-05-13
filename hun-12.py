#swa
a,b=map(int,input().split())
l=[int(i) for i in input().split()]
while b>1:
  n=max(l)
  l.remove(n)
  b=b-1
print(max(l))
