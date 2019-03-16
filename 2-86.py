#wsa
n =int(input())
a = list(map(int,input().split()))
x = a[0]
for i in range(1,n):
    x = x^a[i]
print(x)
