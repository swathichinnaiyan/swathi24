#p
s=input()
s=list(s)
x=[]
l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"]
i=0
while i<len(s):
	for j in range(len(l)):
		if s[i]==l[j]:
			x.append(l[j+3])
	i+=1
for i in range(len(x)):
	print(x[i],end="")
