n=int(input())
i=2
t=3
p=3
for i in range(0,n+1,2):
    if t==1:
        t=2*p
        p=t
    else:
        t=t-1
    #i=i+1
print(t)
