#swa
n=list(map(str,input().split(" ")))
s=input()
count=0
for i in range(0,len(n)):
	if n[i]==s:
		count=count+1
print(count)		
	
