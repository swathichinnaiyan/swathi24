#swa
n=input()
c=0
for i in range(0,len(n)):
    s=n[0:i]+n[i+1::]
    if int(s)%8==0:
        c=1
        break
if c==1:
    print("yes")
else:
    print("no")
