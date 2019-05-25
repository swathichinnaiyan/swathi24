#sw
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
	s=bin(i)[2::]
	l1.append(([s.count("1"),i]))
l1.sort(reverse=True)
for i in range(0,len(l1)):
	print(l1[i][1])
