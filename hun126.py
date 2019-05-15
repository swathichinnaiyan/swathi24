#swa
s=input()
l=s.split(" ")
f=1
for i in range(len(l)):
  if l[i][0].isupper():
    f=1
  else:
    f=0
    break
if f==1:
  print("yes")
else:
  print("no")
