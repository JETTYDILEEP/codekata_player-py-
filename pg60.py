m,n=map(str,input().split())
c=0
for i in m:
  if(i in n):
    c=c+1


if(c>0):
  print('yes')
else:
  print('no')  
