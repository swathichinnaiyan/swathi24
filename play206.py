#swa
s=input()
for i in range(0,len(s)):
	if s[i]<="9" or s[i]<="F":
		a=0
	else:
		a=1
		break
if a==0:
	print("yes")
else:
	print("no")
