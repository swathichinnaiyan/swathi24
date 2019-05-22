#swa
s=input()
k=""
for i in s:
	if s.count(i)>1:
		k=k+i.upper()
	else:
		k=k+i
print(k)
