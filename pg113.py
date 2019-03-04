n=list(map(int,input().split('/')))
if((n[0]<31 and n[0]>1) and (n[1]>0 and n[1]>=1) and n[2]>=1):
  print('yes')
else:
  print('no')
