#multiple
s=int(input())
l1=[]
for i in range(1,6):
    l1.append(s*i)
for i in range(len(l1)-1):
  print(l1[i],end=" ")
print(l1[-1]) 
