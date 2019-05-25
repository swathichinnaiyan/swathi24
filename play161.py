#vowel
n=int(input())
l=[]
a=['a','e','i','o','u']
c=1
for i in range(n):
	s=input()
	l.append(s)
	for i in s:
		if i in a:
			c=1
			break
		else:
			c=0
if c==1:
    print("yes")
else:
    print("no")
