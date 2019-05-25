#s
s1=input()
s2=input()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l1=[]
for i,j in zip(s1,s2):
	l1.append((l.index(i)+1)+(l.index(j)+1))
#print(l1)
for i in range(0,len(l1)):
	if l1[i]>26:
		l1[i]=l1[i]%26
#print(l1)		
for i in l1:
    
	print(l[i-1],end="")
