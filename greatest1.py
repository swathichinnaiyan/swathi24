num1,num2,num3 = map(int, input().split()) 
if (num1>=num2  and num1>=num3):
	print(num1)
elif(num2>=num1 and num2>=num3):
	print(num2)
else:
	print(num3)
	
