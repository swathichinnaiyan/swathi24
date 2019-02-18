#swww
n=int(input())
s=input()
l=["a","e","i","o","u","A","E","I","O","U"]
f=""
for i in s:
	if i not in l:
		f=f+i
print(f[::-1])
