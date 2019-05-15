#swa
n=input()
l=[]
for i in n:
	if i not in l:
		l.append(i)
	else:
		break
print(len(l))
