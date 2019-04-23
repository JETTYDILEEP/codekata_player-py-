class pg151:
  def func(n):
    c=0
    for i in n:
      if(i=='a' or i=='b'):
        c=c+0
      else:
        c=c+1
    if(c==0 or c==1):
      print('yes')
    else:
      print('no')

n=input()
pg151.func(n)'
