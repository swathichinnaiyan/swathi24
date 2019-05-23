#swa
s=input()
for i in range(0,len(s)):
    if s[:i]==s[i+1:]:
        print(s[:i])
        print(s[i+1:])
        c=0
        #break
    else:
        c=1
if c==0:
    print("YES")
else:
    print("NO")
