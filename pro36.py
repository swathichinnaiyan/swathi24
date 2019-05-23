#swa
n = int(input())
a = list(map(int,input().split()))
c = 0
for i in range(0,len(a)-2):
  for j in range(i+1,len(a)-1):
    for k in range(j+1,len(a)):
      if i<j<k and a[i]>a[j]>a[k]:
        c = c+1
print(c)
