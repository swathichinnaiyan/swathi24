from itertools import permutations
s=input()
l=list(permutations(s))
c=0
for i in range(len(l)):
	if l[i]==l[i][::-1]:
		c=1
		print("yes")
		break
if c==0:
	print("no")
 ## 
