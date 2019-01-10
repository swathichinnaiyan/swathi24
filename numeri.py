string=input()

count=0
for i in range(0,len(string)):
	if string[i].isnumeric():
		count=count+1
print(count)		
