#swa
n=input()
l=len(n)
n=list(map(int,n.split("/")))
if l!=10:
    print("no")
else:
    if n[0]<=31 and n[1]<=12:
        print("yes")
    else:
        print("no")
