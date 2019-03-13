def is_Power(x):
  while (x%2== 0):
       x =x/2
  if(x==1):
     print('yes')
  else:
    print('no')

n=int(input())
is_Power(n)
