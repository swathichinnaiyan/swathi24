#swa
a = input("")
b = input("")
l = ""
for i in range(len(a)):
    for j in range(len(a),-1,-1):
        if(a[i:j] in b):
            if(len(a[i:j])>=len(l)):
                l = a[i:j]
print(l)
