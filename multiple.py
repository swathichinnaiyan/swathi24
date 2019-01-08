n=int(input())
l=[]
for i in range(1,6):
    l.append(n*i)
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1]) 
