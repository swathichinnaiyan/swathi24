n,k=map(int,input().split())
s= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
s.sort()
#print(s)
s=s[1:]
#print(s)
#print(s[::3])
s=[i[1] for i in s[:3]]
print(*s)
