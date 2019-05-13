#swa
def fact1(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact

n,k=map(int,input().split(" "))
print(fact1(n)//(fact1(k)*fact1(n-k)))
