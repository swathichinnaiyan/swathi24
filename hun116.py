#
a,b = input().split()
s= ''
k=1
if len(a)>len(b):
  m = len(a)
else:
  m = len(b)
for i in range(0,m):
  try:
    s =s+ a[i]+b[i]
  except IndexError:
    if len(a)>len(b):
      s += a[i]+str(k)
    else:
      s += str(k)+b[i]
    k += 1
print(s)
