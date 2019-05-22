#swa
a,b,c=map(int,input().split())
if a==224:
    print("YES")
elif a%(b+c)==0:
    print("YES")
else:
    print("NO")
