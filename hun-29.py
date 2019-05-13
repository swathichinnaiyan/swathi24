#Swa
n=int(input())
n1=list(map(int,input().split()))
su=[]
su.append(sum(n1))
for i in range(0,n-1):
  a,a1=n1[:i+1],n1[i+1:]
  if sum(a)>sum(a1):
    su.append(sum(a))
  else:
    su.append(sum(a1))
print(max(su))
