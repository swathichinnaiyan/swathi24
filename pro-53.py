#swa
n=input()
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l1=n.lower()
if all (i in l1 for i in l):
	print("yes")
else:
	print("no")
