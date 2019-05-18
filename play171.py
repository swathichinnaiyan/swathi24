#w
s=input()
s=list(s.split(" "))
for i in range(0,len(s)-1):
    if s[i]=="and":
        s[i-1],s[i+1]=s[i+1],s[i-1]
print(*s)
