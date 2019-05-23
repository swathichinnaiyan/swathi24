#s
n=int(input())
l=list(map(int,input().split()))
c=1
for i in l:
    c=c*i
if c%2==0:
    print("even")
else:
    print("odd")
