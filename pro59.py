x,y=map(str,input().split("|"))
c=input()
if len(x)>len(y):
  if len(x)==len(y+c):
    print(x+"|"+y+c)
elif len(x)<len(y):
  if len(x+c)==len(y):
    print(x+c+"|"+y)
    
elif len(x)==len(y) and len(c)>1 or (len(y)or len(x))==0:
  print("Impossible")
  ##
