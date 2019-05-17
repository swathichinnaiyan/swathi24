#Swa
n=input()
s=n[::-1]
t=""
for i in range(0,len(n)-1):
    t=t+s[i]+"-"
print(t+s[len(n)-1])    
    
