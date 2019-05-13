#swa
a=int(input())
b,c=[],[]
for i in range(0,a):
  b=sorted(list(map(int,input().split())))
  c=c+b
print(*sorted(c))
