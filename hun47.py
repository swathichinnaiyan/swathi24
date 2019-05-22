#s
import re
n=input()
r=re.sub(' +', ' ', n)
print(r.strip())
