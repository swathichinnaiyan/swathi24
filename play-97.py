#swa
n=int(input())
l=[]
while n!=0:
    r=n%10
    l.append(r)
    n=n//10
sum1=l[0]+l[-1]
print(sum1)
