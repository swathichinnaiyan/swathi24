#swa
l=list(input())
l=[int(i) for i in l]
s=0
for i in range(len(l)+1):
	s=s+sum(l[:i])
print(s)
