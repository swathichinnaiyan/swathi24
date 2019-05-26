#a
n,k=map(int,input().split())
l=[]
for i in range(n):
	l.append(input())
c=0	
for i in l:
    if l.count(i)==k:
        #print("yes")
        c=c+1
if c>=1:
    print("yes")
else:
    print("no")
    
	
