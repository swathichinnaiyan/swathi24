#swa
n=input()
a=""
for i in range(0,len(n)):
	if n[i].isupper():
		a=a+n[i].lower()
	elif n[i].islower():
		a=a+n[i].upper()
	else:
		a=a+n[i]
print(a)		
		
