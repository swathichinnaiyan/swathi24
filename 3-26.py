#swa
n=int(input())
li=list(input().split())
for i in range(len(li)-1,0,-1):
  print(li[i],end="->")
print(li[0])
