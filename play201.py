#s
def catalan_number(num):
    if num <=1:
         return 1
   
    num1 = 0
    for i in range(num):
        num1 += catalan_number(i) * catalan_number(num-i-1)
    return num1
 
n=int(input())
l=[]
for i in range(0,n+1):
    l.append(catalan_number(n))
print(*l)    
