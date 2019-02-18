#swa
s=input()
s1=""
for i in range(0,len(s)):
	if s[i].islower():
		s1=s1+s[i].upper()
	else:
		s1=s1+s[i].lower()
print(s1)		
		
