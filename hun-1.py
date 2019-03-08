#swa
n=int(input())
l=list(map(int,input().split()))
r=[]
f=""
for i in l:
    if(l.count(i)>1):
        r.append(i)
if(len(r)==0):
    print("unique")
else:
    s=set(r)
    s=list(s)
    s=sorted(s)
    for i in s:
        f=f+str(i)+" "
    print(f.strip())

    
       
