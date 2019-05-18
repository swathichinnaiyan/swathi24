#pali
s=input()
subst=""
f=0
op=[]
if s==s[::-1]:
  op.append(0)
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    subst=s[i:j+1]
    if subst==subst[::-1]:
      op.append(len(s)-len(subst))
     
print(min(op))
