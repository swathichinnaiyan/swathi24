#Swa
from itertools import permutations
a=input()
p=permutations(a)
for i in list(p):
	print(''.join(i))
