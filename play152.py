#Sw
s=input()
c=0
l=["a","e","i","o","u"]
for i in range(0,len(s)-2):
	if s[i] in l and s[i+1] not in l:
		c+=2
		if s[i+1] not in l and s[i+2] in l:
			c+=1
print(c)
