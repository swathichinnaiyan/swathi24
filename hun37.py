#swa
s=input()
x=1
for i in s:
	b=s.replace(i,"",1)
	
	a=b[::-1]
	if b==a:
		x=0
		break
if x==0:
	print("YES")
else:
	print("NO")
