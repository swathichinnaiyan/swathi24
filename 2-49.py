
#swa
n=int(input())
if n>=-2**15+1 and n<=2**15+1:
    print("INT")
elif n>=-2**31+1 and n<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
