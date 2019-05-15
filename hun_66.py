#swa
n=input()
s=input().split()
c=0
p=input()
for i in s:
	if p==i[:len(p)]:
		c+=1
print(c)
