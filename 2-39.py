#swa
d=int(input())
for i in range(0,d):
	if 2**i==d or d==1:
		print("yes")
		break
else:
	print("no")
