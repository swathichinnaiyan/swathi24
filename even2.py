#swa
n=input()
count=0
count1=0
for i in range(0,len(n)):
	if n[i].isalpha():
		count=count+1
	elif n[i].isnumeric():
		count1=count1+1
	else:
		pass
if count!=0 and count1!=0:
	print("Yes")
else:
	print("No")
