#swa
n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1=a1[::-1]
if a1==a2:
    print("yes")
else:
    print("no")
