#swa
s=input()
t=0
for i in range(0,len(s)):
	if int(s[i])%2!=0:
		t=t+int(s[i])
if t%2==0:
	print("E")
else:
	print("O")
		
