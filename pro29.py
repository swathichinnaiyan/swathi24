#s
n=int(input())
l=[]
for i in range(1,n):
    rev=0
    temp=i
    while temp!=0:
        re=temp%10
        rev=rev+re
        temp=temp//10
    if i+rev==n:
        l.append(i)
print(len(l))
for j in range(0,len(l)):
    print(l[j])


        
        
