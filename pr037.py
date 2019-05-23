#swa
n=input()
a=list(map(int,input().split()))
c=0
for i in range(1,len(a)-1):
  if a[i]<a[i+1] and a[i]<a[i-1]:
    c+=1
  elif a[i]>a[i+1] and a[i]>a[i-1]:
    c+=1
print(c)
