#swa
s1,s2,k=input().split()
k=int(k)
c=0
for i in range(len(s1)):
  if s1[i]!=s2[i]:
    c+=1
if c==k:
  print('yes')
else:
  print('no')
