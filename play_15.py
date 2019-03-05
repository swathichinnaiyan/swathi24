#swa
s=input()
t=[]
for i in s:
    t.append(s.count(i))
for i in range(0,len(t)):
    a=max(t)
    if t[i]==a:
        print(s[i])
        break
