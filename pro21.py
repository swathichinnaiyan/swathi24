#ps
n=int(input())
li=list(map(int,input().split()))
c=0
for i in range(1,len(li)):
    if (sum(li[:i]))//len(li[:i])==(sum(li[i:]))//len(li[i:]):
        c+=1
        break
    else:
        c=0
if c>=1:
    print("yes")
else:
    print("no")
