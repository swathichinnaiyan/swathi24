#swa
n=int(input())
k=list(map(int,input().split()))
s=[]
s=[1]*n
for i in range(n):
    if i==0:
        if k[i]>k[i+1]:
            s[i]=s[i]+s[i+1]
    elif i>0:
        if k[i]>k[i-1]:
            s[i]=s[i]+s[i-1]
print(sum(s))
           
