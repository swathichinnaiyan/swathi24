#s
s=input()
s1=input()
u=s+s1
c=0
for i in u:
    if u.count(i)==1:
        c=1
    else:
        c=0
if c==1 and len(u)==26:
    print("complementary")
else:
    print("non-complementary")
