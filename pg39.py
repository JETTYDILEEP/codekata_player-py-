n=int(input())
y=2
if(n==1):
  print('yes')
while(y<=n):
  if(n==y):
    print("yes")
    break
  y=y*2
else:
  print('no')    