n=int(input())
l1=[]
for val in range(0, n): 
      
   
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           l1.append(val)
if n==2:
    print(0)
else:
    print(*l1)           
           
           
