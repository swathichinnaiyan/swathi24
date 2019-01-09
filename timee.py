n=int(input())
if n>60:
  hours = n // 60
  minu=(n %60)
  print(hours,minu)
else:
	print(0,n)
