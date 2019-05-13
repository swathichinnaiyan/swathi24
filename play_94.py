#Swa
n=input()
c=0
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            c=c+1
if c>=1:
    print("yes")
else:
    print("no")
            
