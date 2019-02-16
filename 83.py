#swa
s=input()
o=['/','%']
for i in s:
	if i in o:
		if(i=='/'):
			a=int(s.split(i)[0])
			b=int(s.split(i)[1])
			print(a//b)
		else:
			a=int(s.split(i)[0])
			b=int(s.split(i)[0])
			print(a%b)
