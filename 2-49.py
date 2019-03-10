
#swa
x= input("")
num = int(x.replace(",",""))
if(num>= -2147483648 and num<= 2147483647):
    print("INT")
elif(num>=9223372036854775808 and num<= 9223372036854775807):
    print("LONG LONG")
else:
    print("LONG")
