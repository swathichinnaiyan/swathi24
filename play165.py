#swa
n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
s=[]
c=0
for i in range(0,len(l)):
    if l[i]>k:
        s.append(l[i])
print(s[0])       
            
	    
	    
	
