li=input()
c=0
#li=list(map(int,input().split()))
for i in range(0,len(li)):
    if i!=len(li)-1:
        c=c+int(li[i])**int(li[i+1])
    else:
        c=c+int(li[i])**int(li[0])
print(c)        
