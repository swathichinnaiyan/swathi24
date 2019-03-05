#swa
def isPrime(n):
    c=1
    for i in range(2,n):
        if(n%i==0):
            c=0
            break
    return c
x=int(input())
s=""
l=[]
for i in range(2,x+1):
    if(x%i==0):
        r=isPrime(i)
        if(r==1):
            l.append(i)
for i in sorted(l):
    s=s+str(i)+" "
print(s.strip())
