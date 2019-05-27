#s
n=int(input())
c=0
for i in range(0,n+1):
    for j in range(0,n+1):
        if i*3==n:
            c=c+1
        elif i*7==n:
            c=c+1
        elif (i*3)+(i*7)==n:
            c=c+1
if c>=1:
    print("yes")
else:
    print("no")
        
