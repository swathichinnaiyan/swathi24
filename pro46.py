n=int(input())
l=list(map(int,input().split()))
a_has=0
b_has=0
l.sort(reverse=True)
for i in l:
  s=a_has+i
  if b_has>s:
    a_has=s
  else:
    a_has=b_has
    b_has=s
print(a_has,b_has)
