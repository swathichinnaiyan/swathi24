#swa
n=int(input())
l=[int(x) for x in input().split()]
s=[]
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		for k in range(j+1,len(l)):
			if l[i]+l[j]==l[k]:
				s.append(l[k])
				print(l[i],l[j],l[k])
				break
