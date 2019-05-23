#quasi
n=input()
if n==n[::-1]:
    print("yes")
else:
    a=n.strip("0")
    
    if a==a[::-1]:
        print("yes")
    else:
        a=n.lstrip("0")
        
        if a==a[::-1]:
            print("yes")
        else:
            print("no")
