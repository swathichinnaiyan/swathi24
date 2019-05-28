n,k=input().split()
s=0
if len(n)>len(k):
  n,k=k,n
i=0
while i<len(n):
  s+=(ord(k[i])-ord(n[i]))
  i+=1
for i in range(i,len(k)):
  s+=ord(k[i])-ord('a')+1
print(s)
