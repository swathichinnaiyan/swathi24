#swa
s=input()
s1=""
s2=""
for i in range(0,len(s),2):
    s1=s1+s[i]
for i in range(1,len(s),2):
    s2=s2+s[i]
print(s1,s2)
