#pal
n=input()
l=n[::-1]
s=""
if n==l:
    print(n)
else:
    for i in range(len(n)-1):
        for j in range(i+1,len(n)+1):
            r=n[i:j+1]
    
        if len(r)>len(s) and r==r[::-1]:
            s=r
print(s)
