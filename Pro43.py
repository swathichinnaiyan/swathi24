#swa
n = int(input())
a = list(map(int,input().split()))
c,l = 0,[]
b = [x for x in range(1,n+1)]
for i in a:
  if i in b:
    b.remove(i)
d = 0
for i in range(0,n-1):
  p = a[i]
  for j in range(i+1,n):
    if p == a[j]:
      if p < b[d]:
        a[j] = b[d]
        c += 1
      else:
        a[i] = b[d]
        c += 1
      d += 1
print(c)
print(*a)
