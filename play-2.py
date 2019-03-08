#swa
n=int(input())
l=list(map(int,input().split()))
if l.count(0)==len(l):
    print(0)
else:
    g=sorted(l,reverse=True)
    for i in g:
        print(i,end="")
