#swa
s=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(l.count(i))
n=max(s)
for i in range(0,len(s)):
    if s[i]==n:
        print(l[i])
        break

        
