#swa
n,k=map(int,input().split())
p=[]
s=""
l=list(map(int,input().split()))
for i in range(0,k):
	l.append(l[0])
	l.remove(l[0])
for i in l:
   
        s=s+str(i)+" "
print(s.strip())
	
