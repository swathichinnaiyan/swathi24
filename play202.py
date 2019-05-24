#sw
n=input()
l1=[]
l2=[]
for i in range(0,len(n)):
    if (n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u"):
        l1.append(n[i])
    else:
        l2.append(n[i])
l=l1+l2
for i in range(0,len(l)-1):
    print(l[i],end="")
print(l[-1])    
    
        
        
