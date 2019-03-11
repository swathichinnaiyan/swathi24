#swa
n=int(input())
k=list(map(int,input().split()))
l=list(set(k))
l.sort()
print(l[1]-l[0])
