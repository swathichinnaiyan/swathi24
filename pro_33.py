#swa
s=input()
for i in range(1,len(s)):
	if s[0]<s[i]:
		print(s[i:])
		break
