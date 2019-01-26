s=input()
c=0
for i in range(0,len(s)):
	if (s[i]=="a")or(s[i]=="e") or(s[i]=="i")or(s[i]=="o")or(s[i]=="u"):
		c=c+1
		break
if c!=0:
	print("yes")
else:
	print("no")
	
		
