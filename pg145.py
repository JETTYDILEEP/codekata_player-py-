class pg145:
  def func(n,l):
    t=0
    for i in range(1,n+1):
      if(i in l):
        t=t+1 
      else:
        continue
    if(t==n):
      print('yes')
    else:
      print('no')

n=int(input())
l=[int(x) for x in input().split()]
if(len(l)==n):
  pg145.func(n,l)
