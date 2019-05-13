#swa
n,z = map(str,input().split())
z = int(z)
c =0
for i in range(z):
    if(str(i) in n):
        c+=1
if(c == z):
    print("yes")
else:
    print("no")
