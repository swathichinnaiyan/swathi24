#swa
n=int(input())
rev=0
rem=0
while n!=0:
	rev=n%10
	n=n//10
	rem=(rem*10)+rev
print(rem)
