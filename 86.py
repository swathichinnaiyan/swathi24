s=input()
count=0
count1=0
for i in range(0,len(s)):
	if s[i]!=s[i-1]:
		count=count+1
	else:
		count1=count1+1
if count1>0:
	print("No")
else:
	print("Yes")
		
