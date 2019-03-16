#swa
n=int(input())
l=list(map(int,input().split()))
s=l[0]
for i in range(1,len(l)):
    s=s^l[i]
print(s)
