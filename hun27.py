#pali
a=input()
a=list(a)
if a==a[::-1]:
	while a==a[::-1]:
		a[-1]=""
h=""
for i in a:
	h=h+i
print(h)
