#swa
n=int(input())
sum=0
t=n
while (t!=0):
    rev=t%10
    sum=(rev*rev)+sum
    t=t//10
print(sum)    
