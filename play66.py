a,k=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    if l.count(i)==k:
        print(i)
        break
    
