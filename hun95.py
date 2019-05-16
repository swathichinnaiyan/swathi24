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
    for i in range(0,len(l1)-1):
        print(l1[i],end=" ")
    print(l1[-1])    
           
           
