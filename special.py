n1=input()
c=0
for i in n1:
	if i.isalpha():
		continue
	elif i.isnumeric():
		continue
	elif i==" ":
		continue
	else:
		c=c+1
print(c)
