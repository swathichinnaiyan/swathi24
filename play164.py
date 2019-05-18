n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
l2=[]
s=[]
c=0
for i in range(0,len(l)):
	if l[i]==k:
	   
	    c=c+1
	    
	else:
	    l2.append(l[i])
if c>=1:
    print(k)
else:
    for i in range(0,len(l2)):
        if l2[i]<k:
            s.append(l2[i])
    print(max(s))        
            
	    
	    
	
