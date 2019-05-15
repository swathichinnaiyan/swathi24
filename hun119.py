#swa
a = int(input())
b = [ int(x) for x in input().split()]
c = 0
for i in range(0,len(b)) :
    for j in range(i+1,len(b)) :
        if b[i]<b[j]:
            c=c+1
print(c)
