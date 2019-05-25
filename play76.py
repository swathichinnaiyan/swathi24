#pl
n=int(input())
li=list(map(int,input().split()))
odd=[]
even=[]
for i in li:
  if i%2==0:
    even.append(li.index(i))
  else:
    odd.append(li.index(i))
if len(even)==1:
  print(li[even[0]])
if len(odd)==1:
  print(li[odd[0]])
