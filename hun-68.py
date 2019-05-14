#swa
n=int(input())
l=list(map(int,input().split()))
print((l.index(min(l)))+1,end=" ")
print((l.index(max(l)))+1)
