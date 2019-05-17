#swa
n = input("")
li = list(n)
for i in range(len(li)):
    li[i] = int(li[i])
res = 0
for i in range(len(li)):
    ans = sum(li[:i+1])
    res += ans
print(res)
