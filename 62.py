s=input()
for i in s:
	if i!="1" and i!="0":
		flag=0
		break
	else:
		flag=1
if flag==0:
	print("no")
else:
	print("yes")
		
