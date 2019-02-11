l,b,h=map(int,input().split(" "))

volume=l*b*h

s= (( l * b ) + ( l* h ) + ( b* h ))
s1=s*2
print(s1, end=" ")
print(volume)
