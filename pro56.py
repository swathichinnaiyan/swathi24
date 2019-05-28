n,t=map(int,input().split())
secs=list(map(int,input().split()))
c=0
for i in secs:
  t1=86400-i
  t=t-t1
  c=c+1
  
print(c)
