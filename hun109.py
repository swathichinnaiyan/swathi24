#sw
n=int(input())
l=list(map(str,input().split()))
a=[]
for i in range(0,len(l)):
    a.append(l[i].lower())
for i in range(0,len(a)):
    print(a[i])
