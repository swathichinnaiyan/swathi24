#swa
import math
a,b=map(int,input().split())
s=math.gcd(a,b)
print((a*b)//s)
