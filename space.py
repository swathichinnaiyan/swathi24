s=input()
count=1
for i in range(0,len(s)):
	if s[i]=="." or len(s)+1==" ":
		count=count+1
print(count)		
