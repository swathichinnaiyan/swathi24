#swa
n1=int(input())
arr1= list(map(int, input().split()))
arr1.sort()

for i in range(len(arr1)-1):
	print(arr1[i],end=" ")
print(arr1[-1])
