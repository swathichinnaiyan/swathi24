#Swa
s,k=input().split()
k=int(k)
a=""
for i in range(len(s)):
	if (i+1)%k==0:
		a+=s[i].upper()
	else:
		a+=s[i]
print(a)
