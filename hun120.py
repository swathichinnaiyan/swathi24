#swa
a = int(input())
b = [ int(x) for x in input().split()]
c = 0
for i in range(0,len(b)) :
    for j in range(i+1,len(b)) :
        for k in range(j+1,len(b)) :
            if b[i] + b[j] == b[k] :
                c += 1
print(c)
